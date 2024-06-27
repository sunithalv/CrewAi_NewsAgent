from crew import crew_news
from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json
import uvicorn
import os
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Body(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate") 
async def generate_report(input_text: str = Form(...)):  
    response = crew_news.kickoff(inputs={'topic':input_text})
    # print(response)
    # answer = response['result']
    response_data = jsonable_encoder(json.dumps({"answer": response}))
    res = Response(response_data)
    return res

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)