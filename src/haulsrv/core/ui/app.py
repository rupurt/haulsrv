from datetime import datetime

from quart import Quart, render_template

app = Quart(__name__)


@app.get("/")
async def root():
    return await render_template('index.html', hello='world')


@app.get("/probes/live")
async def probes_live_show():
    return {"now": datetime.now()}
