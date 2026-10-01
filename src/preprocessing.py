# cleaning, encoding, feature engineering
import pandas as pd
import os
from config.config import RAW_DATA_FILE, PROCESSED_DATA_FILE, PROCESSED_DIR

class Preprocessor:
    def __init__(self, file_path: str = RAW_DATA_FILE):
        self.df = pd.read_excel(file_path)

    def replace_missing_with_unknown(self, column: str):
        if column in self.df.columns:
            missing_before = self.df[column].isnull().sum()
            self.df[column] = self.df[column].fillna("Unknown")
            missing_after = self.df[column].isnull().sum()

            print(f"\nColumn: {column}")
            print(f"Missing values before: {missing_before}")
            print(f"Missing values after: {missing_after}")
            print("Replacement complete")
        else:
            print(f"Column '{column}' not found in dataset.")

        return self.df

    def save_processed(self, filename: str = PROCESSED_DATA_FILE):
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        self.df.to_excel(filename, index=False)
        print(f"\nCleaned dataset saved to: {filename}")
        return filename
