import pytest

from haulsrv.core.api import app


@pytest.mark.asyncio
async def test_show_root():
    client = app.test_client()
    response = await client.get("/")
    assert response.status_code == 302
    assert response.location == "/docs"
