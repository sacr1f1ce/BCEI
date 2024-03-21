from typing import Union
import subprocess
from fastapi import FastAPI, Request, Form
 
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
 
templates = Jinja2Templates(directory="templates")
 
app = FastAPI()
 
app.mount("/static",StaticFiles(directory="static",html=True),name="static")
 
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
 
@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
 
@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/buy")
def buy(request: Request):
    return templates.TemplateResponse("buy.html", {"request": request})

@app.get("/run-script")
async def run_script():
    subprocess.run(["python", "script.py"])
    return {"message": "Script executed successfully"}

@app.get("/marketplace")
def buy(request: Request):
    return templates.TemplateResponse("marketplace.html", {"request": request})

@app.get("/run-marketplace")
async def run_script():
    subprocess.run(["python", "marketplace.py"])
    return {"message": "Script executed successfully"}

