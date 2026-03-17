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
def load_accounts():
    accsvc.add_accounts()


@cli.command()
def print_accounts():
    accsvc.print_accounts()


@cli.command()
def full_cycle():
    accsvc.init_database()
    accsvc.add_accounts()
    accsvc.print_accounts()


if __name__ == '__main__':
    cli()
