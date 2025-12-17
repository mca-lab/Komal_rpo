# Big Data Project- Bike Sharing Analysis

## Project Overview
This project explores and analyzes the Bike Sharing Dataset using Python, PySpark, and Docker.
The workflow includes:

1. Data ingestion from public datasets (Bike Sharing Dataset: day.csv and hour.csv)
2. Data cleaning and integration
3. Analysis and visualization
4. Reproducible Docker-based setup for data collection and processing

## research question 
How do weather conditions, seasonal changes, and time (hour/day) influence bike rental demand in the dataset?

---

## Project Workflow

### Module 1. Data Collection & Ingestion
**Objective:** Automate downloading datasets and storing them for processing.

- Fetched two datasets dynamically from GitHub URLs:
  - day.csv
  - hour.csv
- Stored datasets in `data/raw/`
- Docker container ensures reproducible data fetching environment

**Deliverables:**
- Dockerfile + requirements.txt
- src/fetch_data.py
- data/raw/ populated when container runs

---

### Module 2. Data Cleaning & Integration
**Objective:** Prepare raw data for analysis using PySpark.

**Tasks:**
- Loaded raw datasets into PySpark
- Handled missing values, inconsistent formats, and duplicates
- Aggregated hourly dataset to daily counts for analysis
- Merged day-level and hourly-level datasets for comprehensive insights
- Stored processed data in data/processed/
- Docker container ensures reproducible cleaning pipeline

**Deliverables:**
- Dockerfile + requirements.txt for cleaning
- src/clean_data.py
- data/processed/ ready for analysis

---

### Module 3. Data Analysis & Visualization
**Objective:** Explore and analyze cleaned datasets to answer the research question.

**Tasks:**
-Loaded processed datasets in Jupyter Notebook
- Performed descriptive statistics, correlation analysis, aggregations, and scatter/regression plots
- Visualized using Matplotlib and Seaborn
- Documented findings and interpretations in notebook cells

**Deliverables:**
- Loaded processed datasets in Jupyter Notebook
- Performed descriptive statistics, correlation analysis, aggregations, and scatter/regression plots
- Visualized using Matplotlib and Seaborn
- Documented findings and interpretations in notebook cells

---
**Key Insights**

- Bike rentals increase with higher temperature and lower humidity
- Rentals are highest during working days compared to holidays/weekends
- Seasonal trends significantly impact rental demand (summer and fall peak)
- Hourly trends show morning and evening peaks

---

## Technologies
- Python
- PySpark
- Matplotlib and  Seaborn
- Docker(for Modules 1 & 2)

---

## Notes
- Module 1 and Module 2 require Docker for reproducibility
- Module 3 is executed in Jupyter Notebook (no Docker required)
- End goal: automated pipeline from data fetching → cleaning → analysis → insights

