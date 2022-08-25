import click

@click.command()
@click.option(
    "-s",
    "--search",
    help="This flag searches wikipedia with the provided arg"
 )
@click.option(
    "-d",
    "--download",
    help="wiki -d [wikipedia_url]"
 )
@click.option(
    "-df",
    "--downlfolder",
    help="select/create a downloads path to receive pages"
 )
@click.option(
    "-v", 
    "--view",
    help="View pages stored in downloads path"
)
# def cli(): needs to be passed a string as an arg, 
# for each option.
def cli(search,
        download, 
        downlfolder, 
        view):
    # This displays the menu
    # and command flags for the program.
    click.echo("WikiCLI: The command line interface for Wikipedia")

if __name__ == "__main__":
    cli()
