from pathlib import Path

import typer
from rich.pretty import pprint
from typing_extensions import Annotated

from haulsrv.cli.main import app
from haulsrv.settings import default_config, read_settings


@app.command()
def settings(
    config: Annotated[
        Path,
        typer.Option(
            default_config,
            is_eager=True,
            help="path to config file",
        ),
    ],
):
    settings = read_settings(config)
    pprint(settings)
