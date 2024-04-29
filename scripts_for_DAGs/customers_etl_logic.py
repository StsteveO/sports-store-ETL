import pandas as pd
import sqlalchemy as db

engine = db.create_engine('postgresql://xosxlxys:uoHxehFCCr8M_exJ6ETuRJoKvqlUvER2@mouse.db.elephantsql.com/xosxlxys')

def main():
    customers = pd.read_excel('/home/steveomari62/sports-store-ETL/store_raw_data/H+ Sport Customers.xlsx')
    customers = customers[~customers.duplicated(['FirstName', 'LastName', 'Email', 'Phone'], keep='first')]
    customers.to_sql('customers', engine, if_exists='replace', index=False)

    print('Customers ETL script completed.')


