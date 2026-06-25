from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "insightstream",
    "retries": 1,
}

DBT_DIR = "/opt/airflow/dbt_project"
DATA_DIR = "/opt/airflow/data"

with DAG(
    dag_id="insightstream_elt_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2026, 6, 1),
    catchup=False,
    tags=["insightstream"],
) as dag:

    load_raw_data = BashOperator(
        task_id="load_raw_data_to_snowflake",
        bash_command=f"cd {DATA_DIR} && python load_to_snowflake.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test",
    )

    load_raw_data >> dbt_run >> dbt_test
