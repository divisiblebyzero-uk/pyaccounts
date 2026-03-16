# Functional Requirements

## Chart of Accounts

1. Ingest Chart of Accounts (CoA) from input file eg accounts.csv
2. Categorise at a high level into [EQUITY, ASSET, BANK, LIABILITY, CREDIT, INCOME, EXPENSE]
3. Build a nested structure as per CoA

## Transaction processing into Journals

1. Ingest transactions from input file eg transactions.csv
2. Infer the missing account details (debit account, credit account) based on known information (which account the transactions refer to - given as part of upload process, and matching of the transaction description)
3. Store as Journals

## Statements

Produce reports:

1. Profit and Loss:
    1. For each month in a given year,
    2. Sum the amounts in the INCOME accounts
    3. Sum the amounts in the EXPENSE accounts
    4. Show the above totals, plus the difference as Profit/Loss

## File formats

### accounts.csv

| Type | CoA Path | Account Name | Account Code | Description | Currency | Placeholder |
|------|----------|--------------|--------------|-------------|----------|-------------|
|ASSET | Assets   | Assets       | A       | Asset parent|GBP       | T           |
|ASSET | Assets/CurrentAssets | Current Assets | CA | Current Assets | GBP | T |
|BANK  | Assets/CurrentAssets/CurrentAccountSole | Sole Bank Account | SBA | Sole Bank Account | GBP | F |

### transactions.csv

| Date | Description | Amount |
|------|-------------|--------|
| 01/01/2001 | Rent | -500.00 |
| 01/01/2001 | Salary | 2000.00 |
