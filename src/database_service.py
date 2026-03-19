import sqlite3
import os
import account_service as account_service
import transaction_service as transaction_service
dbname = '../test/accounting.db'


def get_connection():
    return sqlite3.connect(dbname)


def init_database():
    account_service.create_accounts_table()
    transaction_service.create_transactions_table()


def drop_database():
    os.remove(dbname)
