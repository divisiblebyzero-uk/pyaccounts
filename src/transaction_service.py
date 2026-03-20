import database_service as db
import pandas as pd
import account_service
import locale

locale.setlocale(locale.LC_ALL, '')

def create_transactions_table():
    with db.get_connection() as connection:
        cursor = connection.cursor()
        create_transactions_table_query = '''
                                      create table if not exists Transactions
                                      (
                                          id integer primary key autoincrement,
                                          date date not null,
                                          description text not null,
                                          amount number not null,
                                          accountId integer not null,
                                          direction integer not null
                                      ); \
                                      '''
        cursor.execute(create_transactions_table_query)
        connection.commit()


def get_mapping(mappings, description):
    poss_match = mappings[mappings['description'] == description]
    if poss_match.size > 0:
        return poss_match.iloc[0].account_id
    else:
        return 0

def add_transactions(transactions_file, transaction_account_mapping_file, account_path):
    mappings = pd.read_csv(transaction_account_mapping_file)
    mappings['account_id'] = mappings.apply(lambda row:
                                     account_service.get_account_by_path(row.account_path)[0]
                                     ,axis=1)

    account_id = account_service.get_account_by_path(account_path)[0]

    with db.get_connection() as connection:
        df = pd.read_csv(transactions_file, names=['date', 'description', 'amount'], header=None)

        transactions = []

        for index, row in df.iterrows():
            other_account_id = get_mapping(mappings, row.description)
            raw_amount = locale.atof(row.amount)
            abs_amount = abs(raw_amount)
            print(f"{row.date}, {row.description}, {raw_amount}, {account_id}, {other_account_id}")
            if raw_amount < 0:
                transactions.append([row.date, row.description, abs_amount, account_id, -1])
                transactions.append([row.date, row.description, abs_amount, other_account_id, 1])
            else:
                transactions.append([row.date, row.description, abs_amount, account_id, 1])
                transactions.append([row.date, row.description, abs_amount, other_account_id, -1])


        transactions_df = pd.DataFrame(transactions, columns=['date', 'description', 'amount', 'accountId', 'direction'])
        transactions_df.to_sql('Transactions', connection, if_exists='append', index=False)


def print_transactions():
    with db.get_connection() as connection:
        select_account_query = '''
                               select *
                               from Transactions; \
                               '''
        df = pd.read_sql_query(select_account_query, connection)

        print("All transactions: ")
        print(df)

