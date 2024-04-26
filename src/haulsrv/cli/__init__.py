from haulsrv.cli.main import app
from haulsrv.cli import init
from haulsrv.cli import start
# from haulsrv.cli import settings

__all__ = [
    "app",
    "init",
    "start",
    # "settings",
]

if __name__ == "__main__":
    app()
