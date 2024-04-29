# Sports Store ETL

## Summary
A mock store selling sports equipment requires data-driven help in figuring out where to open their new branch.

I've downloaded four datasets in excel forms respresenting data from the stores customers, employees, products, and orders made. 

> [!IMPORTANT]
> Jupyter Notebook was used in testing python code line by line prior to creating DAGs in Apache Airflow

- Pandas (the Python library) was used to work with, and transform the raw data.

## Bugs and Solutions

### Bug 1
- Bug: Extracting the raw data via pandas threw and error
- Solution: Python was missing the openpyxl library; `pip install openpyxl`