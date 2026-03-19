import database_service as db
import pandas as pd
import account_service


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
                                          debitAccountId integer not null,
                                          creditAccountId integer not null
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


def add_transactions(transactions_file, transaction_account_mapping_file, debit_account_path):
    mappings = pd.read_csv(transaction_account_mapping_file)
    mappings['account_id'] = mappings.apply(lambda row:
                                     account_service.get_account_by_path(row.account_path)[0]
                                     ,axis=1)


    debit_account_id = account_service.get_account_by_path(debit_account_path)[0]

    with db.get_connection() as connection:
        df = pd.read_csv(transactions_file, names=['date', 'description', 'amount'], header=None)
        #df.rename(columns={'Merchant/Description': 'description', 'Debit/Credit': 'amount'}, inplace=True)
        df.insert(0, 'debitAccountId', debit_account_id)

        df['creditAccountId'] = df.apply(lambda row:
                                            get_mapping(mappings, row['description'])#mappings.loc[mappings['description'] == row['description']]['account_path']
                                            , axis=1)

        df.to_sql('Transactions', connection, if_exists='append', index=False)


def print_transactions():
    with db.get_connection() as connection:
        select_account_query = '''
                               select *
                               from Transactions; \
                               '''
        df = pd.read_sql_query(select_account_query, connection)

        print("All transactions: ")
        print(df)

