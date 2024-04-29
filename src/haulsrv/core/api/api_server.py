import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config as HypercornConfig
from typerutils import LogLevel

from haulsrv.core.api.app import app
from haulsrv.core.worker_class import WorkerClass


class ApiServer:
    config: HypercornConfig
    loop: asyncio.AbstractEventLoop
    shutdown_event: asyncio.Event

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        shutdown_event: asyncio.Event,
        host: str = "0.0.0.0",
        port: int = 8080,
        log_level: LogLevel = LogLevel.INFO,
        worker_class: WorkerClass = WorkerClass.UVLOOP,
    ):
        config = HypercornConfig()
        config.bind = [f"{host}:{port}"]
        config.loglevel = log_level.value
        config.worker_class = worker_class.value
        self.config = config
        self.loop = loop
        self.shutdown_event = shutdown_event

    def serve(self):
        return self.loop.create_task(
            serve(
                app,
                self.config,
                shutdown_trigger=self.shutdown_event.wait,
            )
        )
