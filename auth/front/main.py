import os

import uvicorn as uvicorn
from db import get_logins_statistic
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from mqtt import beep
from mqtt import client as mqtt_client

app = FastAPI()


templates = Jinja2Templates(directory=os.path.join(os.getcwd(), 'templates'))


@app.get('/', response_class=HTMLResponse)
def show_logins_statistic(request: Request):
    recs = get_logins_statistic()

    return templates.TemplateResponse('index.html', {'request': request, 'recs': recs})


@app.post('/')
def beep_(request: Request):
    beep(mqtt_client)


if __name__ == '__main__':
    uvicorn.run(app)
