import pytest

from haulsrv.core.api import app


@pytest.mark.asyncio
async def test_api_v1_cluster_list():
    client = app.test_client()
    response = await client.get("/api/v1/cluster")
    assert response.status_code == 200
    result = await response.get_json()
    assert result["todo"] == "todo..."
