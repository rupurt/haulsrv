from typing import Optional

from typerutils import LogLevel

from haulsrv.core.api import ApiServer
from haulsrv.core.ui import UiServer
from haulsrv.core.worker_class import WorkerClass


class ServerConfig:
    host: str
    port: int
    enabled: bool

    def __init__(self, host: str, port: int, enabled: bool):
        self.host = host
        self.port = port
        self.enabled = enabled


class Server:
    api_server: Optional[ApiServer]
    ui_server: Optional[UiServer]

    def __init__(
        self,
        api: ServerConfig = ServerConfig("0.0.0.0", 8080, True),
        ui: ServerConfig = ServerConfig("0.0.0.0", 8081, True),
        log_level: LogLevel = LogLevel.INFO,
        worker_class: WorkerClass = WorkerClass.UVLOOP,
    ):
        if api.enabled:
            self.api_server = ApiServer(
                host=api.host,
                port=api.port,
                log_level=log_level,
                worker_class=worker_class,
            )
        if ui.enabled:
            self.ui_server = UiServer(
                host=ui.host,
                port=ui.port,
                log_level=log_level,
                worker_class=worker_class,
            )

    def serve(self) -> None:
        if self.api_server:
            self.api_server.serve()
        if self.ui_server:
            self.ui_server.serve()

    # def close(self) -> None:
    #     if self.api_server:
    #         self.api_server.close()
    #     if self.ui_server:
    #         self.ui_server.close()
