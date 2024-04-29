import pandas as pd
import sqlalchemy as db

engine = db.create_engine('postgresql://xosxlxys:uoHxehFCCr8M_exJ6ETuRJoKvqlUvER2@mouse.db.elephantsql.com/xosxlxys')

def main():
    products = pd.read_excel('/home/steveomari62/sports-store-ETL/store_raw_data/H+ Sport products.xlsx')
    products['Price'] = (products['Price'] / 0.92).round(2)
    products.rename(columns={'Price' : 'Price (dollars)'}, inplace= True)
    products.to_sql('products', engine, if_exists='replace', index=False)


    print('Products ETL script completed.')


