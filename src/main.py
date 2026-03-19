import click
import account_service as account_service
import transaction_service as transaction_service
import database_service as db


@click.group()
def cli():
    pass


def init_db():
    click.echo("Initializing database...")
    db.init_database()


def drop_db():
    click.echo("Dropping database...")
    db.drop_database()


def load_accounts(accounts_file):
    click.echo(f"Loading accounts from file {accounts_file}...")
    account_service.add_accounts(accounts_file)


def print_accounts():
    click.echo("Printing accounts...")
    account_service.print_accounts()

def load_transactions(transactions_file, transaction_account_mapping_file, debit_account_path):
    click.echo(f"Loading transactions from file {transactions_file} into account {debit_account_path} using mapping file {transaction_account_mapping_file}...")
    transaction_service.add_transactions(transactions_file, transaction_account_mapping_file, debit_account_path)


def print_transactions():
    click.echo("Printing transactions...")
    transaction_service.print_transactions()

@cli.command()
@click.option('--accounts_file', default='../test/accounts.csv')
@click.option('--transactions_file', default='../test/transactions.csv')
@click.option('--transaction_account_mapping_file', default='../test/accountmappings.csv')
@click.option('--debit_account_path', default='Assets:Current Assets:Current Account (Sole)')
def full_cycle(accounts_file, transactions_file, transaction_account_mapping_file, debit_account_path):
    click.echo(f"Performing full cycle with accounts_file: {accounts_file}")
    drop_db()
    init_db()
    load_accounts(accounts_file)
    print_accounts()

    load_transactions(transactions_file, transaction_account_mapping_file, debit_account_path)
    print_transactions()


if __name__ == '__main__':
    cli()
