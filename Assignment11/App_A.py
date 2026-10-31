"""
App_A - a small "greeting" command-line tool.
Built for click==7.0 ONLY.
"""
import click
from click._bashcomplete import get_choices

COLOURS = ["red", "green", "blue", "yellow"]

def complete_colour(ctx, args, incomplete):
    return [c for c in COLOURS if c.startswith(incomplete)]

@click.command()
@click.option("--name", default="World", help="Who to greet.")
@click.option("--colour", default="green", help="Text colour.",
              autocompletion=complete_colour)
def cli(name, colour):
    click.secho(f"[App_A | click {click.__version__}] Hello, {name}!", fg=colour)
    suggestions = [c for c, _help in get_choices(cli, "app_a", ["--colour"], "b")]
    click.echo(f"Tab-completion suggestions for '--colour b': {suggestions}")

if __name__ == "__main__":
    cli()
