[WikiCLI]

This program should search Wikipedia in a CLI interface. To then possibly download a given wiki page from its URL; After downloaded, it should view a selected page from a specified download path.

***Search Option***
- @click.option()
- should include a descriptive &&
  simple flag.
- should include help text with 
  Clicks default --help flag.

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