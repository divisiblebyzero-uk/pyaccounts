import click
import accountservice as accsvc


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    accsvc.init_database()


@cli.command()
def drop_db():
    accsvc.drop_database()


@cli.command()
@click.argument('accounts_file')
def load_accounts(accounts_file):
    accsvc.add_accounts()


@cli.command()
def print_accounts():
    accsvc.print_accounts()


@cli.command()
@click.argument('accounts_file')
def full_cycle(accounts_file):
    click.echo(f"Performing full cycle with accounts_file: {accounts_file}")
    accsvc.drop_database()
    accsvc.init_database()
    accsvc.add_accounts(accounts_file)
    accsvc.print_accounts()


if __name__ == '__main__':
    cli()
