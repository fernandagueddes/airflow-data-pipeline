import pandas as pd
from sqlalchemy import create_engine


def extract():
    print("📥 Extract: lendo arquivo CSV...")
    df = pd.read_csv("/opt/airflow/data/users.csv")
    print(f"Linhas carregadas: {len(df)}")
    return df


def transform(df):
    print("🔧 Transform: filtrando usuários com idade > 30...")
    df = df[df["age"] > 30]
    print(f"Linhas após transformação: {len(df)}")
    return df


def load(df):
    print("💾 Load: salvando dados no Postgres...")

    engine = create_engine(
        "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
    )

    df.to_sql(
        "users_clean",
        engine,
        if_exists="replace",
        index=False
    )

    print("✅ Dados salvos na tabela users_clean!")


def run_etl():
    print("🚀 Iniciando pipeline ETL")

    df = extract()
    df = transform(df)
    load(df)

    print("🏁 Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    run_etl()