# Data Pipeline with Airflow, Docker and PostgreSQL

An end-to-end ETL data pipeline built with **Python, Apache Airflow, PostgreSQL, Pandas, SQLAlchemy, and Docker**.

The pipeline extracts user data from a CSV file, applies data validation and transformation rules, and loads the processed dataset into a PostgreSQL database. Apache Airflow orchestrates the workflow, while Docker provides a reproducible containerized environment.

## Architecture

```text
users.csv
    │
    ▼
┌───────────────┐
│    Extract    │
│  Read CSV     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Transform   │
│ Validate Age  │
│ Filter > 30   │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     Load      │
│  PostgreSQL   │
└───────────────┘

Orchestrated by Apache Airflow
```

## Pipeline Overview

The pipeline follows the traditional **Extract, Transform, Load (ETL)** pattern.

### Extract

The pipeline reads user data from:

```text
data/users.csv
```

The extraction step:

- Validates that the source file exists
- Reads the CSV file using Pandas
- Creates a DataFrame for further processing

### Transform

The transformation step applies basic data quality and business rules:

- Validates that the `age` column exists
- Converts age values to numeric format
- Removes invalid or missing age values
- Filters users older than 30

### Load

The transformed dataset is loaded into PostgreSQL using **SQLAlchemy** and Pandas.

The resulting table is:

```text
users_clean
```

## Airflow Orchestration

Apache Airflow orchestrates the ETL workflow through the DAG:

```text
etl_users_pipeline
```

The DAG uses a `BashOperator` to execute the ETL script inside the Airflow container.

```text
Airflow DAG
     │
     ▼
run_etl_script
     │
     ▼
etl_users.py
     │
     ▼
Extract → Transform → Load
```

The DAG is configured for manual execution, making it easy to trigger and monitor the pipeline through the Airflow web interface.

## Project Structure

```text
.
├── dags/
│   └── etl_users_dag.py
│
├── data/
│   └── users.csv
│
├── etl/
│   └── etl_users.py
│
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Technologies

- **Python** — ETL pipeline logic
- **Pandas** — data extraction, validation, and transformation
- **SQLAlchemy** — database connection and data loading
- **PostgreSQL** — storage of processed data
- **Apache Airflow** — workflow orchestration
- **Docker** — containerized execution environment
- **Docker Compose** — multi-container environment management

## Docker Environment

The project uses Docker Compose to run the complete environment.

The main services are:

- **PostgreSQL** — stores Airflow metadata and the processed user dataset
- **Airflow Init** — initializes the Airflow metadata database and admin user
- **Airflow Webserver** — provides the Airflow web interface
- **Airflow Scheduler** — schedules and executes DAG tasks

## Running the Project

### Prerequisites

Make sure you have installed:

- Docker
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/fernandagueddes/airflow-data-pipeline.git
cd airflow-data-pipeline
```

### 2. Start the environment

```bash
docker compose up
```

Docker Compose starts PostgreSQL and the required Airflow services.

### 3. Access Apache Airflow

Open:

```text
http://localhost:8080
```

Default credentials:

```text
Username: airflow
Password: airflow
```

### 4. Run the pipeline

In the Airflow interface, locate the DAG:

```text
etl_users_pipeline
```

Trigger the DAG manually.

Airflow executes the ETL script, which processes the CSV dataset and loads the resulting data into the PostgreSQL `users_clean` table.

## Data Flow

```text
data/users.csv
      │
      ▼
Extract with Pandas
      │
      ▼
Validate Data
      │
      ▼
Convert Age to Numeric
      │
      ▼
Remove Invalid Ages
      │
      ▼
Filter Age > 30
      │
      ▼
Load with SQLAlchemy
      │
      ▼
PostgreSQL
users_clean
```

## Skills Demonstrated

This project demonstrates practical experience with:

- ETL pipeline development
- Workflow orchestration with Apache Airflow
- Data validation and transformation with Pandas
- PostgreSQL integration
- SQLAlchemy database connections
- Dockerized data environments
- Airflow DAG development
- Data loading into relational databases
- Git version control
