from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
import pycorrector as correct


class Text(BaseModel):
    content: str

class CorrectContent(BaseModel):
    wrong: str
    right: str
    start_pos: int
    end_pos: int

class Correction(BaseModel):
    origin: str
    correct: List[CorrectContent]

app = FastAPI()

@app.post("/correct", response_model=Correction)
async def create_item(text: Text):
    result = correct.correct(text.content)
    return Correction(origin=result[0], correct=[CorrectContent(wrong=r[0], right=r[1], start_pos=r[2], end_pos=r[3]) for r in result[1]])