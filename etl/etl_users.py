import os

import pandas as pd
from sqlalchemy import create_engine


DATA_PATH = "/opt/airflow/data/users.csv"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow",
)


def extract():
    """
    Extract user data from the source CSV file.
    """
    print("Extracting data from CSV...")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Source file not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    print(f"Rows extracted: {len(df)}")

    return df


def transform(df):
    """
    Filter users older than 30 years.
    """
    print("Transforming data...")

    required_columns = ["age"]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    df["age"] = pd.to_numeric(
        df["age"],
        errors="coerce",
    )

    df = df.dropna(
        subset=["age"]
    ).copy()

    df = df[
        df["age"] > 30
    ].copy()

    print(
        f"Rows after transformation: {len(df)}"
    )

    return df


def load(df):
    """
    Load transformed data into PostgreSQL.
    """
    print("Loading data into PostgreSQL...")

    engine = create_engine(
        DATABASE_URL
    )

    df.to_sql(
        "users_clean",
        engine,
        if_exists="replace",
        index=False,
    )

    print(
        "Data successfully loaded into users_clean."
    )


def run_etl():
    """
    Execute the complete ETL pipeline.
    """
    print("Starting ETL pipeline...")

    df = extract()
    df = transform(df)
    load(df)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_etl()
