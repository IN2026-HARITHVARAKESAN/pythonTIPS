"""
App_B - a small "greeting" command-line tool.
Built for click==8.0 ONLY.
"""
import click
from click.shell_completion import CompletionItem

COLOURS = ["red", "green", "blue", "yellow"]

def complete_colour(incomplete):
    return [CompletionItem(c, help=f"print in {c}") for c in COLOURS if c.startswith(incomplete)]

@click.command()
@click.option("--name", default="World", help="Who to greet.")
@click.option("--colour", default="green", help="Text colour.",
              shell_complete=complete_colour)
def cli(name, colour):
    click.secho(f"[App_B | click {click.__version__}] Hello, {name}!", fg=colour)

    items = complete_colour("b")
    click.echo(f"Tab-completion suggestions for '--colour b': {[i.value for i in items]}")

if __name__ == "__main__":
    cli()
