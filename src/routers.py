from fastapi import APIRouter, Request, Depends, Response, Cookie
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uuid
from .crud import get_or_create_city, record_city_search, get_city_stats, get_user_history
from .weather import get_weather_data, get_city_suggestions
from .database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, user_id: str = Cookie(default=None), db: Session = Depends(get_db)):
    if not user_id:
        user_id = str(uuid.uuid4())
        response = templates.TemplateResponse("index.html", {"request": request, "last_city": None})
        response.set_cookie("user_id", user_id)
        return response

    history = get_user_history(user_id, db)
    last_city = history[0] if history else None
    return templates.TemplateResponse("index.html", {"request": request, "last_city": last_city})


@router.get("/api/weather")
async def weather(city: str, user_id: str = Cookie(default=None), db=Depends(get_db)):
    city_obj = get_or_create_city(db, city)
    if user_id:
        record_city_search(db, user_id, city_obj.id)
    data = await get_weather_data(city)
    return JSONResponse(content=data)


@router.get("/api/stat")
def stat(db=Depends(get_db)):
    return get_city_stats(db)


@router.get("/api/history")
def history(user_id: str = Cookie(default=None), db=Depends(get_db)):
    return get_user_history(user_id, db)


@router.get("/api/suggest")
async def suggest(q: str):
    return await get_city_suggestions(q)
