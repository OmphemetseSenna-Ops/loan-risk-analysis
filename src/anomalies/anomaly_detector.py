import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config.config import PROCESSED_DATA_FILE

class AnomalyDetector:
    def __init__(self, file_path: str = PROCESSED_DATA_FILE):
        self.df = pd.read_excel(file_path)

    # Detect outliers using IQR method.
    def numeric_outliers(self, column: str):
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
        print(f"\n{column}: Outliers detected: {outliers.shape[0]}")
        return outliers

    # Detect rare categories (<1% frequency).
    def categorical_anomalies(self, column: str, threshold=0.01):
        freq = self.df[column].value_counts(normalize=True)
        rare = freq[freq < threshold]
        print(f"\n{column}: Rare categories:\n{rare}")
        return rare

    # Detect invalid/future dates.
    def date_anomalies(self, column: str):
        self.df[column] = pd.to_datetime(self.df[column], errors="coerce")
        future_dates = self.df[self.df[column] > pd.Timestamp.today()]
        print(f"\n{column}: Future dates detected: {future_dates.shape[0]}")
        return future_dates

    # Check if there is no user duplicates
    def check_duplicate_ids(df):
        dup_ids = df[df['id'].duplicated()]
        print(f"Duplicate IDs: {dup_ids.shape[0]}")
        return dup_ids

    def check_negative_values(df, cols):
        for col in cols:
            neg = df[df[col] < 0]
            if not neg.empty:
                print(f"{col} has {neg.shape[0]} negative values")
        return

    def check_future_dates(df, date_cols):
        for col in date_cols:
            future = df[df[col] > pd.Timestamp.today()]
            print(f"{col} has {future.shape[0]} future dates")
        return

    def check_status_vs_payment(df):
        anomalies = df[(df['loan_status'] == "Fully Paid") & (df['total_payment'] == 0)]
        print(f"Loan status/payment mismatch: {anomalies.shape[0]}")
        return anomalies
