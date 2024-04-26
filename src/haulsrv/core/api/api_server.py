from typerutils import LogLevel

from haulsrv.core.api.app import app
from haulsrv.core.worker_class import WorkerClass


class ApiServer:
    host: str
    port: int
    log_level: LogLevel
    worker_class: WorkerClass

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 8080,
        log_level: LogLevel = LogLevel.INFO,
        worker_class: WorkerClass = WorkerClass.UVLOOP,
    ):
        self.host = host
        self.port = port
        self.log_level = log_level
        self.worker_class = worker_class

    def serve(self) -> None:
        app.run(host=self.host, port=self.port)

    # def close(self):
    #     app.close()
