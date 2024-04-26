import pytest

from haulsrv.core.api import app


@pytest.mark.asyncio
async def test_show_probes_live():
    client = app.test_client()
    response = await client.get("/probes/live")
    assert response.status_code == 200
    result = await response.get_json()
    assert result["now"] is not None
