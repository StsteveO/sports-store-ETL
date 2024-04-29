from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from orders_etl_logic import main

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2024, 4, 20),
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
}

dag = DAG(
    'updated_orders',
    default_args = default_args,
    description = 'Orders ETL DAG',
    schedule_interval = '@daily',
)

run_etl = PythonOperator(
    task_id = 'run_etl',
    python_callable = main,
    dag = dag,
)

run_etl