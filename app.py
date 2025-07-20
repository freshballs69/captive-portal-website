from sanic import Sanic
from sanic_ext import render

app = Sanic('evil-captive-portal')

app.static('/static', 'static', directory_view=True)

@app.get('/')
async def index(req):
    return await render("index.html")


@app.post('/')
async def handle_form(req):
    return await render("success.html")