import typer
from typer import Typer


from grader.cli import gforms

app: Typer = typer.Typer()


app.add_typer(gforms.app, name="gforms")


def grader() -> None:
    app()


if __name__ == "__main__":
    app()
