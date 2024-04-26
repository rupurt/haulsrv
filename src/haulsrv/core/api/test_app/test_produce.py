import pytest

from haulsrv.core.api import app

@pytest.mark.asyncio
async def test_create_api_v1_produce():
    client = app.test_client()
    response = await client.post("/api/v1/produce")
    assert response.status_code == 201
    result = await response.get_json()
    assert result["todo"] == "todo..."
