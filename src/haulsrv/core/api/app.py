from datetime import datetime

from quart import Quart, redirect
# from quart_schema import QuartSchema, validate_request, validate_response
from quart_schema import QuartSchema

app = Quart(__name__)
QuartSchema(app)


@app.get("/")
async def root():
    return redirect("/docs")


@app.get("/probes/live")
async def probes_live_show():
    return {"now": datetime.now()}


@app.post("/api/v1/topics")
async def api_v1_topics_create():
    return {"id": "todo..."}, 201


@app.get("/api/v1/topics")
async def api_v1_topics_list():
    return {"topics": []}


@app.get("/api/v1/topics/<id>")
async def api_v1_topics_show(id):
    return {"topic": {"id": "todo..."}}


@app.delete("/api/v1/topics/<id>")
async def api_v1_topics_delete(id):
    return {"todo": "todo..."}


@app.post("/api/v1/produce")
async def api_v1_produce_create():
    return {"todo": "todo..."}, 201


@app.get("/api/v1/consume")
async def api_v1_consume_list():
    return {"records": []}


@app.get("/api/v1/cluster")
async def api_v1_cluster_list():
    return {"todo": "todo..."}
