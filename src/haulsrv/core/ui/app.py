from datetime import datetime

from quart import Quart

app = Quart(__name__)


@app.get("/")
async def hello():
    return "hello world! - UI"


@app.get("/probes/live")
async def probes_live_show():
    return {"now": datetime.now()}
