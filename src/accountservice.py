from faker import Faker
import sqlite3
import os
import pandas as pd

fake = Faker(['en_GB'])
dbname = '../test/accounting.db'

def getConnection():
    return sqlite3.connect(dbname)

def initDatabase():
    createAccountsTable()

def createAccountsTable():
    with getConnection() as connection:
        cursor = connection.cursor()
        create_accounts_table_query = '''
        create table if not exists Accounts (
            id integer primary key autoincrement,
            type text not null,
            path text not null,
            name text not null,
            code text not null,
            description text not null,
            currency text not null,
            placeholder text not null
        );
            '''
        cursor.execute(create_accounts_table_query)
        connection.commit()

def addAccounts():
    with getConnection() as connection:
        cursor = connection.cursor()

        insert_account_query = '''
insert into Accounts (type, path, name, code, description, currency, placeholder)
values (?, ?, ?, ?, ?, ?, ?)
'''

        account_data = [(fake.name(), fake.text(), fake.text(), fake.text(), fake.text(), fake.currency_code(), 'F') for _ in range(5)]
        cursor.executemany(insert_account_query, account_data)
        connection.commit()

def printAccounts():
    with getConnection() as connection:
        select_account_query = '''
select * from Accounts;
'''
        df = pd.read_sql_query(select_account_query, connection)

        print("All accounts: ")
        print(df);

def dropDatabase():
    os.remove(dbname)