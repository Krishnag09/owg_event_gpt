import os
from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

load_dotenv()
router = APIRouter()


@router.get("/desc", description="get test response", )
async def expand():
    client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=[
                                                    {"role": "system",
                                                     "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                                                    {"role": "user",
                                                     "content": "Compose a poem that explains the concept of recursion in programming."}
                                                ])
    print(completion)
    return completion
