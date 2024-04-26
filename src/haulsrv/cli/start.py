from pathlib import Path

import typer
from typerutils import LogLevel
from typing_extensions import Annotated

from haulsrv.cli import app
from haulsrv.core import Server, ServerConfig
from haulsrv.settings import default_config, read_settings


def conf_callback(
    ctx: typer.Context,
    param: typer.CallbackParam,
    value: str,
):
    ctx.default_map = ctx.default_map or {}
    if value:
        try:
            settings = read_settings(Path(value))
            print(settings)
            default_map = {
                "api_host": settings.api.host,
                "api_port": settings.api.port,
                "api_enabled": settings.api.enabled,
                "ui_host": settings.ui.host,
                "ui_port": settings.ui.port,
                "ui_enabled": settings.ui.enabled,
                "log_level": settings.log_level,
            }
            ctx.default_map.update(default_map)
        except Exception:
            pass
    return value


@app.command()
def start(
    api_host: Annotated[
        str,
        typer.Option(
            help="host for api server to listen on",
        ),
    ],
    api_port: Annotated[
        int,
        typer.Option(
            help="port for api server to listen on",
        ),
    ],
    ui_host: Annotated[
        str,
        typer.Option(
            help="host for ui server to listen on",
        ),
    ],
    ui_port: Annotated[
        int,
        typer.Option(
            help="port for ui server to listen on",
        ),
    ],
    log_level: Annotated[
        LogLevel,
        typer.Option(
            help="log level to use in servers",
        ),
    ],
    api_enabled: Annotated[
        bool,
        typer.Option(
            help="enable/disable api server",
        ),
    ] = True,
    ui_enabled: Annotated[
        bool,
        typer.Option(
            help="enable/disable ui server",
        ),
    ] = True,
    config: Annotated[
        Path,
        typer.Option(
            callback=conf_callback,
            is_eager=True,
            help="path to config file that will be created",
        ),
    ] = default_config,
):
    api = ServerConfig(api_host, api_port, api_enabled)
    ui = ServerConfig(ui_host, ui_port, ui_enabled)
    server = Server(api=api, ui=ui, log_level=log_level)
    server.serve()
