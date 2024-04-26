import pytest

from haulsrv.core.api import app


@pytest.mark.asyncio
async def test_create_api_v1_topics():
    client = app.test_client()
    response = await client.post("/api/v1/topics")
    assert response.status_code == 201
    result = await response.get_json()
    assert result["id"] is not None


@pytest.mark.asyncio
async def test_list_api_v1_topics():
    client = app.test_client()
    response = await client.get("/api/v1/topics")
    assert response.status_code == 200
    result = await response.get_json()
    assert result["topics"] == []


@pytest.mark.asyncio
async def test_show_api_v1_topics():
    client = app.test_client()
    response = await client.get("/api/v1/topics/todo")
    assert response.status_code == 200
    result = await response.get_json()
    assert result["topic"] == {
        "id": "todo...",
    }


@pytest.mark.asyncio
async def test_delete_api_v1_topics():
    client = app.test_client()
    response = await client.delete("/api/v1/topics/todo")
    assert response.status_code == 200
