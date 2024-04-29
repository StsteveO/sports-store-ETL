import pandas as pd
import sqlalchemy as db

engine = db.create_engine('postgresql://xosxlxys:uoHxehFCCr8M_exJ6ETuRJoKvqlUvER2@mouse.db.elephantsql.com/xosxlxys')

def main():
    employees = pd.read_excel('/home/steveomari62/sports-store-ETL/store_raw_data/H+ Sport Employees.xlsx', sheet_name='Employees')
    employees = employees.drop(columns=['New Salary', 'Tax Rate', 0.0291])
    employees.to_sql('employees', engine, if_exists='replace', index=False)

    print('Employees ETL script completed.')


