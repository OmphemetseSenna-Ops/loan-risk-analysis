# Loan Risk Analysis

A data science project focused on understanding and predicting loan default risk using borrower and loan characteristics. The workflow includes data extraction, exploratory analysis, preprocessing, model training, and result interpretation for credit risk assessment.

## Overview
This project is designed to help analyze financial loan data and build a prediction pipeline for assessing credit risk. It combines data quality checks, feature engineering, and machine learning models to support better lending decisions and deeper insight into borrower behavior.

## Objectives
- Extract and clean loan data from a public dataset source
- Profile the dataset to understand missing values, distributions, and quality issues
- Preprocess features for modeling
- Train and evaluate risk models for loan default prediction
- Visualize key trends in borrower and loan attributes
- Produce explainable insights for business and analytical stakeholders

## Tech Stack
- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- KaggleHub
- Jupyter and Python scripts

## Project Workflow
1. Dataset retrieval and extraction
2. Data profiling and quality assessment
3. Feature preprocessing and transformation
4. Model training and validation
5. Performance evaluation and explainability
6. Reporting and visualization of insights

## Repository Structure
- `main.py` – main execution entry point
- `src/` – modular project logic for preprocessing, modeling, explainability, and analysis
- `datasets/` – raw and processed loan data
- `reports/` – generated analysis outputs and summaries
- `tests/` – unit tests for validation logic

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd loan-risk-analysis
```

### 2. Create a virtual environment
```bash
python -m venv loanENV
```

On Windows:
```bash
loanENV\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Project
```bash
python main.py
```

This runs the project pipeline, including data loading and analysis tasks defined in the application workflow.

## Data
The project uses a financial loan dataset, typically sourced from Kaggle, to analyze applicant and loan characteristics and predict potential default behavior.


## Notes
This project is intended for data science and credit-risk analysis research and learning. It is not a production lending decision system and should be validated with domain-specific business rules before deployment.

