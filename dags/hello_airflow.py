from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def say_hello():
    print("Olá, Airflow! ✅ Estou rodando dentro do Docker.")


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule=None,  # roda só quando você clicar "play"
    catchup=False,
    tags=["tutorial"],
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )