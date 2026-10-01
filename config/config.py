import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASETS_DIR = os.path.join(BASE_DIR, "datasets")
RAW_DIR = os.path.join(DATASETS_DIR, "raw")
PROCESSED_DIR = os.path.join(DATASETS_DIR, "processed")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

RAW_DATA_FILE = os.path.join(RAW_DIR, "financial_loan.xlsx")
PROCESSED_DATA_FILE = os.path.join(PROCESSED_DIR, "financial_loan_cleaned.xlsx")
