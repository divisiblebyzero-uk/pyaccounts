import database_service as db
import pandas as pd


def check_balanced():
    get_balanced_query_drcr = '''
    select
        sum(case when direction ==  1 then amount end) as DR,
        sum(case when direction == -1 then amount end) as CR
    from
        transactions;'''
    get_balanced_query = '''
    select
        sum(direction*amount)
    from
        transactions;'''

    with db.get_connection() as connection:
        print(pd.read_sql_query(get_balanced_query_drcr, connection))
        print(pd.read_sql_query(get_balanced_query, connection))

def report_balance_sheet():
    get_balance_sheet_sql = '''
    select
        accountId,
        accounts.path,
        sum(amount * direction * normal) as balance
    from
        transactions
        left join accounts on accountId = accounts.id
    group by
        path
    order by
        accountId,
        path;
    '''
    with db.get_connection() as connection:
        print(pd.read_sql_query(get_balance_sheet_sql, connection))