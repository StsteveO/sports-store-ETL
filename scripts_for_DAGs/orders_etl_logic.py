import pandas as pd
import sqlalchemy as db

engine = db.create_engine('postgresql://xosxlxys:uoHxehFCCr8M_exJ6ETuRJoKvqlUvER2@mouse.db.elephantsql.com/xosxlxys')

def main():
    orders = pd.read_excel('/home/steveomari62/sports-store-ETL/store_raw_data/H+ Sport orders.xlsx')
    orders = orders.drop(columns=['CustomersComment', 'SalespersonsComment'])
    orders.to_sql('orders', engine, if_exists='replace', index=False)


    print('Orders ETL script completed.')


