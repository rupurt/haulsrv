import pytest

from haulsrv.core.api import app


@pytest.mark.asyncio
async def test_list_api_v1_consume():
    client = app.test_client()
    response = await client.get("/api/v1/consume")
    assert response.status_code == 200
    result = await response.get_json()
    assert result["records"] == []
