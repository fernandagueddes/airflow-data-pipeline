from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="etl_users_pipeline",
    description="Extract, transform, and load user data into PostgreSQL",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "postgresql"],
) as dag:

    run_etl = BashOperator(
        task_id="run_etl_script",
        bash_command="python /opt/airflow/etl/etl_users.py",
    )
