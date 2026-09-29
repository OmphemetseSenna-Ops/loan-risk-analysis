import pandas as pd
import matplotlib.pyplot as plt

class DataQualityVisualizer:
    def __init__(self, file_path: str):
        # Initialize with path to raw dataset.
        self.df = pd.read_excel(file_path)

    def missing_visualization(self):
        # Plot pie chart of missing vs available values (overall).
        total = self.df.size
        missing = self.df.isnull().sum().sum()
        available = total - missing

        labels = ["Available Data", "Missing Data"]
        values = [available, missing]

        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct="%1.1f%%", colors=["#4CAF50", "#F44336"])
        plt.title("Overall Data Quality")
        plt.show()

    def missing_barplot(self):
        # Bar plot of missing values per column.
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]

        if not missing.empty:
            plt.figure(figsize=(10, 5))
            missing.plot(kind="bar", color="#F44336")
            plt.title("Missing Values per Column")
            plt.ylabel("Count")
            plt.show()
        else:
            print("No missing values found.")
