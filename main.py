from fastapi import FastAPI, Request
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.routing import APIRouter
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="SWIM")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    client_host = request.client.host
    return templates.TemplateResponse(
        request, name="index.html", context={"title": "test", "current_year": 2024}
    )
