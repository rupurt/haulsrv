import asyncio
import signal
from typing import Any, Optional

import uvloop
from quartutils import AsyncTaskServer, TaskServerConfig

from haulsrv.core.api import ApiServer
from haulsrv.core.ui import UiServer


class HaulServer(AsyncTaskServer):
    """
    todo...
    """

    def __init__(
        self,
        api_config: Optional[TaskServerConfig],
        ui_config: Optional[TaskServerConfig],
    ):
        uvloop.install()
        loop = asyncio.get_event_loop()
        loop.add_signal_handler(signal.SIGTERM, self.signal_handler())
        shutdown_event = asyncio.Event()
        servers = []
        if api_config:
            servers.append((ApiServer, api_config))
        if ui_config:
            servers.append((UiServer, ui_config))
        super().__init__(loop, shutdown_event, servers)

    def signal_handler(self):
        def _signal_handler(*_: Any) -> None:
            self.shutdown_event.set()

        return _signal_handler
