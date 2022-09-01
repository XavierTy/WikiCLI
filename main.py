import click 
from click_aliases import ClickAliasedGroup

@click.group(cls=ClickAliasedGroup)
def cli():
    """WikiCLI: The CLI for wikipedia"""

@cli.group('search', cls=ClickAliasedGroup)
def search():
    """Manages the api call to wikipedia."""
    click.echo("This is working: %s")


if __name__ == "__main__":
    cli("--help".split())