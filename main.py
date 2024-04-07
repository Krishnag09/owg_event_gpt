from fastapi import FastAPI
from fastapi import APIRouter
from routers.event import router as event_router
# from routers.weather_data import router as weather_router

router = APIRouter()
app = FastAPI()

app.include_router(event_router)
