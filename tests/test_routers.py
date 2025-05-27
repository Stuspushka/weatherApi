import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8000"


@pytest.mark.asyncio
async def test_suggest():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/api/suggest?q=London")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_weather_existing_city():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/api/weather?city=London")
        assert response.status_code == 200
        json = response.json()
        assert "temperature" in json or "error" in json

@pytest.mark.asyncio
async def test_stat():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/api/stat")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_history_without_cookie():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/api/history")
        assert response.status_code in (200, 422, 400)

@pytest.mark.asyncio
async def test_history_with_cookie():
    async with AsyncClient(base_url=BASE_URL, cookies={"user_id": "test-user"}) as client:
        await client.get("/api/weather?city=Paris")
        response = await client.get("/api/history")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_suggest_empty_query():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/api/suggest?q=")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

