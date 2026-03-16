from dataclasses import dataclass
@dataclass
class Account:
    type: str
    path: str
    accountName: str
    accountCode: str
    description: str
    currency: str
    placeholder: str
    
import csv
with open('../test/accounts.csv', newline='') as csvfile:
    accounts = csv.reader(csvfile, delimiter=",")
    for row in accounts:
        print(row[0])