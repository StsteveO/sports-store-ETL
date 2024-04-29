## Summary
A mock store selling sports equipment requires data-driven help in figuring out where to open their new branch.

I've downloaded four datasets in excel forms respresenting data from the stores customers, employees, products, and orders made. 

> [!IMPORTANT]
> Jupyter Notebook was used in testing python code line by line prior to creating DAGs in Apache Airflow

- Pandas (the Python library) was used to import, work with, and transform the raw data; cleaning, standardizing, removing duplicates, etc.
- A PostgreSQL database on ElephantSQL is used to create, read, update, and delete data from the web browser.
- SQLAlchemy (the Python Library) was used to connect and interact with our database.

Querying the database allowed me to see the branch where the majority of Sport Store's customers shop.

![customer database](/home/steveomari62/sports-store-ETL/assets/db_new_location.png)

## Bugs and Solutions

### Bug 1
- <ins>Bug</ins>: Extracting the raw data via pandas threw and error
- <ins>Solution</ins>: Python was missing the openpyxl library; `pip install openpyxl`

### Bug 2
- <ins>Bug</ins>: Creating a new engine with SQLAlchemy threw and error
    - <ins>Bug 2b</ins>: Attempting to install the missing psycopg2 library, `pip install psycopg2`, threw another error. This is because psycopg2 requires pg_config from the PostgreSQL development files to be installed in my system.
- <ins>Solution</ins>: Install the binary package psycopg2-binary which does not require compiling; `pip install psycopg2-binary`