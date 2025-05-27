import httpx

async def get_weather_data(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    async with httpx.AsyncClient() as client:
        geo_response = await client.get(url)
        geo_data = geo_response.json()
        if not geo_data.get("results"):
            return {"error": "City not found"}
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&hourly=temperature_2m&current_weather=true"
        )
        weather_response = await client.get(weather_url)
        weather_data = weather_response.json()
        return {
            "city": location["name"],
            "temperature": weather_data["current_weather"]["temperature"],
            "units": "°C"
        }


async def get_city_suggestions(query: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=5"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if "results" in data:
            return [r["name"] for r in data["results"]]
        return []
