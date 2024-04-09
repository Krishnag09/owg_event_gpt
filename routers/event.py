import os
from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

load_dotenv()
router = APIRouter()


@router.get("/desc/{event_details}", description="get test response", )
async def expand(event_details: str):
    client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=[
                                                    {"role": "system",
                                                     "content": "You are a regular young professional, write 100-200 words encouraging people to join an outdoor event at provided venue and activities. Write plain and casual"},
                                                    {"role": "user",
                                                     "content": f"Write an event desc using {event_details}"}
                                                ])
    return completion
