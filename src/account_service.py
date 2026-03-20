import sqlite3
import os
import pandas as pd
import database_service as db

def create_accounts_table():
    with db.get_connection() as connection:
        cursor = connection.cursor()
        create_accounts_table_query = '''
                                      create table if not exists Accounts
                                      (
                                          id integer primary key autoincrement,
                                          type text not null,
                                          path text not null,
                                          name text not null,
                                          code text,
                                          description text,
                                          currency text not null,
                                          placeholder text not null,
                                          normal integer not null
                                      ); \
                                      '''
        cursor.execute(create_accounts_table_query)
        connection.commit()


def add_accounts(accounts_file):
    with db.get_connection() as connection:
        df = pd.read_csv(accounts_file)
        df.to_sql('Accounts', connection, if_exists='append', index=False)
        connection.commit()


def print_accounts():
    with db.get_connection() as connection:
        select_account_query = '''
                               select *
                               from Accounts; \
                               '''
        df = pd.read_sql_query(select_account_query, connection)

        print("All accounts: ")
        print(df)


def get_account_by_path(account_path):
    with db.get_connection() as connection:
        select_account_query = "select * from Accounts where path = ?"
        cur = connection.cursor()
        acct = cur.execute(select_account_query, (account_path,)).fetchall()[0]
        return acct