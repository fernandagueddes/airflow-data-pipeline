# Data Pipeline with Airflow, Docker and Postgres

## Project Overview

This project implements a simple data pipeline using Apache Airflow for orchestration, Python for ETL processing, and PostgreSQL for data storage. The entire environment runs inside Docker containers.

The pipeline reads user data from a CSV file, performs a transformation, and loads the processed data into a PostgreSQL database.

## Architecture

CSV file → Python ETL → PostgreSQL → Orchestrated by Airflow

## Technologies Used

- Python
- Apache Airflow
- PostgreSQL
- Docker
- Docker Compose
- Pandas
- SQLAlchemy

## Pipeline Steps

1. Extract  
   Read data from a CSV file.

2. Transform  
   Filter users with age greater than 30.

3. Load  
   Save the transformed data into the PostgreSQL table `users_clean`.

## Project Structure
