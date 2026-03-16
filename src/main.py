import click
import accountservice as accsvc

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    accsvc.initDatabase()

@cli.command()
def drop_db():
    accsvc.dropDatabase()

@cli.command()
def load_accounts():
    accsvc.addAccounts()

@cli.command()
def print_accounts():
    accsvc.printAccounts()

@cli.command()
def full_cycle():
    accsvc.initDatabase()
    accsvc.addAccounts()
    accsvc.printAccounts()

if __name__ == '__main__':
    cli()
