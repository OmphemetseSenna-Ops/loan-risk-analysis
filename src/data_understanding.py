# Understanding the dataset, Uncover Relationships, Detect Anomalies and its characteristics is crucial before diving into preprocessing. This module provides a DataProfiler class to facilitate initial data exploration.

from ast import Return

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataProfiler:
    def __init__(self, file_path: str):
        # Initialize with path to raw dataset.
        self.df = pd.read_excel(file_path)

    ## Section 1: Dataset Overview
    def get_summary(self):
        # Summary of the dataset.
        print("\nDataset Summary:")
        print(self.df.describe(include='all'))
        return self.df.describe(include='all')


    def get_shape(self):
        # Shape of the dataset.
        print(f"\nDataset Shape: {self.df.shape}")
        return self.df.shape

    def get_data_types(self):
        # Data types of each column.
        print("\nData Types:")
        print(self.df.dtypes)
        return self.df.dtypes

    def preview_data(self, n=10):
        # Preview first n rows.
        print(f"\nPreviewing first {n} rows of the dataset:")
        print(self.df.head(n))
        return self.df.head(n)


    ## Section 2: Data Quality Checks
    def missing_summary(self):
        # Return table with total, missing, and available counts per column
        total = len(self.df)
        summary = pd.DataFrame({
            "Column": self.df.columns,
            "Total Records": total,
            "Missing": self.df.isnull().sum().values,
        })
        summary["Available"] = summary["Total Records"] - summary["Missing"]
        print("\nData Quality Summary:")
        print(summary)

        return summary

    def duplicates(self):
        # Check for duplicate rows.
        dup_count = self.df.duplicated().sum()
        print(f"\nDuplicate Rows: {dup_count}")
        return dup_count


    ## Section 3: Column Profiling
    def get_categorical_columns(self):
        # Identify categorical columns and return them.
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        print(f"\nCategorical Columns ({len(categorical_cols)}):")
        print(categorical_cols)
        return categorical_cols


    def get_numeric_columns(self):
        # Identify numeric columns and return them.
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        print(f"\nNumeric Columns ({len(numeric_cols)}):")
        print(numeric_cols)
        return numeric_cols

    def categorical_encoding_overview(self, max_values=10):
        # Suggesting encoding methods for categorical columns based on distinct counts.
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        summary = []

        for col in categorical_cols:
            distinct_vals = self.df[col].dropna().unique()
            distinct_count = len(distinct_vals)
            sample_vals = distinct_vals[:max_values]

            # Dynamic encoding suggestion based on distinct count
            if distinct_count == 2:
                encoding = "Binary Encoding"
            elif 3 <= distinct_count <= 10:
                encoding = "One-Hot Encoding"
            elif distinct_count > 10:
                encoding = "High Cardinality → Target/Hash Encoding"
            else:
                encoding = "Check Column (possible ID/constant)"

            summary.append({
                "Column": col,
                "Distinct Count": distinct_count,
                "Distinct Values (sample)": list(sample_vals),
                "Suggested Encoding": encoding
            })

        summary_df = pd.DataFrame(summary)
        print("\nCategorical Encoding Overview:")
        print(summary_df)

        return summary_df