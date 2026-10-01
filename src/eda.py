# eda
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config.config import PROCESSED_DATA_FILE

class EDA:
    def __init__(self, file_path: str = PROCESSED_DATA_FILE):
        self.df = pd.read_excel(file_path)

    # Overview
    def dataset_overview(self):
        print("\nDataset Shape:", self.df.shape)
        print("\nColumn Types:\n", self.df.dtypes)
        print("\nFirst 5 Rows:\n", self.df.head())

    # Numeric Analysis
    def numeric_summary(self):
        print("\nNumeric Summary:\n", self.df.describe())

        numeric_cols = self.df.select_dtypes(include=['int64','float64']).columns
        self.df[numeric_cols].hist(figsize=(14, 10), bins=30, edgecolor="black")

        plt.suptitle("Numeric Feature Distributions", fontsize=16)

        for ax, col in zip(plt.gcf().axes, numeric_cols):
            mean_val = self.df[col].mean()
            median_val = self.df[col].median()
            ax.axvline(mean_val, color="red", linestyle="--", label=f"Mean={mean_val:.2f}")
            ax.axvline(median_val, color="blue", linestyle=":", label=f"Median={median_val:.2f}")
            ax.legend()

        plt.tight_layout()
        plt.show()

    # Correlation Analysis
    def correlation_heatmap(self):
        numeric_df = self.df.select_dtypes(include=['int64','float64'])
        id_like = [col for col in numeric_df.columns if "id" in col.lower()]
        numeric_df = numeric_df.drop(columns=id_like, errors="ignore")

        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap (Numeric Only, IDs Excluded)")
        plt.show()


    # Date Handling
    def date_summary(self):
        date_cols = [col for col in self.df.columns if "date" in col.lower()]
        for col in date_cols:
            try:
                self.df[col] = pd.to_datetime(self.df[col], errors="coerce")
                plt.figure(figsize=(8, 4))
                self.df[col].dt.year.value_counts().sort_index().plot(kind="bar")
                plt.title(f"Distribution of {col} (by Year)")
                plt.xlabel("Year")
                plt.ylabel("Count")
                plt.show()
            except Exception as e:
                print(f"Skipping {col}: {e}")

    # Categorical Analysis
    def categorical_summary(self):
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        summary = []
        for col in categorical_cols:
            distinct_count = self.df[col].nunique()
            summary.append({"Column": col, "Distinct Count": distinct_count})
            plt.figure(figsize=(6, 4))
            sns.countplot(x=col, data=self.df, order=self.df[col].value_counts().index)
            plt.xticks(rotation=45)
            plt.title(f"Distribution of {col}")
            plt.show()
        return pd.DataFrame(summary)

    # Target Analysis
    def target_distribution(self, target_col="loan_status"):
        print("\nTarget Distribution:\n", self.df[target_col].value_counts())
        sns.countplot(x=target_col, data=self.df)
        plt.title("Loan Status Distribution")
        plt.show()
