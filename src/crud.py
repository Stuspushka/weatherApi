from .models import City, SearchHistory
from sqlalchemy.orm import Session
from sqlalchemy import func


def get_or_create_city(db: Session, city_name: str):
    city = db.query(City).filter(func.lower(City.name) == city_name.lower()).first()
    if not city:
        city = City(name=city_name)
        db.add(city)
        db.commit()
        db.refresh(city)
    return city


def record_city_search(db: Session, user_id: str, city_id: int):
    entry = SearchHistory(user_id=user_id, city_id=city_id)
    db.add(entry)
    db.commit()


def get_city_stats(db: Session):
    results = (
        db.query(City.name, func.count(SearchHistory.id).label("count"))
        .join(SearchHistory)
        .group_by(City.id)
        .order_by(func.count(SearchHistory.id).desc())
        .all()
    )
    return [{"city": name, "count": count} for name, count in results]


def get_user_history(user_id: str, db: Session):
    entries = (
        db.query(City.name)
        .join(SearchHistory)
        .filter(SearchHistory.user_id == user_id)
        .order_by(SearchHistory.timestamp.desc())
        .all()
    )
    return [e[0] for e in entries]
