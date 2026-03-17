from faker import Faker
import sqlite3
import os
import pandas as pd
import csv

fake = Faker(['en_GB'])
dbname = '../test/accounting.db'


def get_connection():
    return sqlite3.connect(dbname)


def init_database():
    create_accounts_table()


def create_accounts_table():
    with get_connection() as connection:
        cursor = connection.cursor()
        create_accounts_table_query = '''
                                      create table if not exists Accounts
                                      (
                                          id
                                          integer
                                          primary
                                          key
                                          autoincrement,
                                          type
                                          text
                                          not
                                          null,
                                          path
                                          text
                                          not
                                          null,
                                          name
                                          text
                                          not
                                          null,
                                          code
                                          text,
                                          description
                                          text,
                                          currency
                                          text
                                          not
                                          null,
                                          placeholder
                                          text
                                          not
                                          null
                                      ); \
                                      '''
        cursor.execute(create_accounts_table_query)
        connection.commit()


def add_accounts(accounts_file):


    with get_connection() as connection:
        df = pd.read_csv(accounts_file)
        df.to_sql('Accounts', connection, if_exists='append', index=False)
        connection.commit()


def print_accounts():
    with get_connection() as connection:
        select_account_query = '''
                               select *
                               from Accounts; \
                               '''
        df = pd.read_sql_query(select_account_query, connection)

        print("All accounts: ")
        print(df);


def drop_database():
    os.remove(dbname)
