import pandas as pd
from config.config import PROCESSED_DATA_FILE


class RiskAnalysis:
    def __init__(self, file_path: str = PROCESSED_DATA_FILE):
        self.df = pd.read_excel(file_path)

    # Check for duplicate loan IDs
    def duplicate_loan_ids(self, sample_size=5):
        duplicates = self.df[self.df['id'].duplicated(keep=False)].copy()
        print(f"Duplicate loan IDs: {len(duplicates)}")

        sample = duplicates[['id', 'member_id', 'loan_status', 'loan_amount',
            'issue_date', 'loan_status']
        ].head(sample_size)

        print("\nSample anomalies:\n", sample.to_string(index=False))

        return duplicates


    # Check for loan IDs shared across multiple members
    def loan_ids_shared_by_members(self, sample_size=5):
        loan_member_counts = self.df.groupby('id')['member_id'].nunique()
        shared_loans = loan_member_counts[loan_member_counts > 1].index
        anomalies = self.df[self.df['id'].isin(shared_loans)].copy()

        print(f"Loan IDs shared across multiple members: {len(shared_loans)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_status', 'loan_amount', 'issue_date']
        ].head(sample_size)

        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies



    # Check for duplicate member_id and loan id combinations
    def duplicate_member_loans(self, sample_size=5):
        duplicates = self.df[self.df.duplicated(subset=['member_id', 'id'], keep=False)].copy()
        print(f"Duplicate member_id + loan_id combinations: {len(duplicates)}")

        sample = duplicates[
            ['member_id', 'id', 'loan_status', 'loan_amount', 'issue_date']
        ].head(sample_size)

        print("\nSample anomalies:\n", sample.to_string(index=False))

        return duplicates


    # Check for invalid loan amounts (NaN or <= 0)
    def invalid_loan_amounts(self, sample_size=5):
        anomalies = self.df[
            self.df['loan_amount'].isna() | (self.df['loan_amount'] <= 0)].copy()
        print(f"Invalid loan amounts: {len(anomalies)}")

        sample = anomalies[['id', 'member_id', 'loan_amount', 'loan_status', 'issue_date']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for invalid annual income (NaN or <= 0)
    def invalid_annual_income(self, sample_size=5):
        anomalies = self.df[
            self.df['annual_income'].isna() | (self.df['annual_income'] <= 0)].copy()
        print(f"Invalid annual income: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'annual_income', 'loan_amount', 'loan_status']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for invalid interest rates (NaN, <= 0, or > 100)
    def invalid_interest_rates(self, sample_size=5):
        anomalies = self.df[
            self.df['int_rate'].isna() | (self.df['int_rate'] <= 0) | (self.df['int_rate'] > 100)].copy()
        print(f"Invalid interest rates: {len(anomalies)}")

        sample = anomalies[['id', 'member_id', 'int_rate', 'loan_amount', 'loan_status']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for suspicious DTI values (NaN, < 0, or > max_dti)
    def suspicious_dti(self, sample_size=5, max_dti=100):
        anomalies = self.df[
            self.df['dti'].isna() | (self.df['dti'] < 0) | (self.df['dti'] > max_dti)
        ].copy()
        print(f"Suspicious DTI values: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'dti', 'annual_income', 'loan_amount', 'loan_status']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for invalid installments (NaN or <= 0)
    def invalid_installments(self, sample_size=5):
        anomalies = self.df[self.df['installment'].isna() | (self.df['installment'] <= 0)
        ].copy()
        print(f"Invalid installments: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_amount', 'installment', 'int_rate', 'term']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for invalid total payments (NaN or < 0)
    def invalid_total_payments(self, sample_size=5):
        anomalies = self.df[self.df['total_payment'].isna() | (self.df['total_payment'] < 0)
        ].copy()
        print(f"Invalid total payments: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_amount', 'total_payment', 'loan_status']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for invalid date sequences (last_payment_date < issue_date), check whether dates occur in a logical sequence.
    def invalid_date_sequence(self, sample_size=5):
        anomalies = self.df[
            (self.df['last_payment_date'].notna()) & (self.df['issue_date'].notna()) &
            (self.df['last_payment_date'] < self.df['issue_date'])
        ].copy()
        print(f"Loans where last payment date occurs before issue date: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'issue_date', 'last_payment_date', 'next_payment_date', 'loan_status']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check for next payment date occurring before last payment date
    def next_payment_before_last_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['next_payment_date'].notna()) &
            (self.df['last_payment_date'].notna()) &
            (self.df['next_payment_date'] < self.df['last_payment_date'])
        ].copy()
        print(f"Next payment date before last payment date: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_status', 'last_payment_date', 'next_payment_date']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Active loans without a next payment date
    def active_loans_without_next_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['loan_status'] == "Current") & (self.df['next_payment_date'].isna())
        ].copy()
        print(f"Active loans without next payment date: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_status', 'loan_amount', 'total_payment', 'installment', 'issue_date', 'last_payment_date']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies

    

    # Check whether fully paid loans have a next payment date
    def status_vs_next_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['loan_status'] == "Fully Paid") & (self.df['next_payment_date'].notna())
        ]
        print(f"Fully Paid loans with next payment date: {anomalies.shape[0]}")
        sample = anomalies[['id','member_id','loan_status','loan_amount', 'total_payment','installment','last_payment_date','next_payment_date']].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))
        return anomalies


    # Fully Paid loans without a next payment date
    def fully_paid_without_next_payment(self, sample_size=5):
        anomalies = self.df[(self.df['loan_status'] == "Fully Paid") & (self.df['next_payment_date'].isna())]
        print(f"Fully Paid loans without next payment date: {len(anomalies)}")

        sample = anomalies[['id','member_id','loan_status','loan_amount', 'total_payment','installment','last_payment_date','next_payment_date']].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies

    # Check whether fully paid loans have no last payment date
    def fully_paid_without_last_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['loan_status'] == "Fully Paid") &
            (self.df['last_payment_date'].isna())
        ].copy()
        print(f"Fully Paid loans without last payment date: {len(anomalies)}")

        sample = anomalies[
            ['id', 'member_id', 'loan_status', 'loan_amount', 'total_payment', 'last_payment_date']
        ].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check whether fully paid loans have total payments less than the loan amount
    def status_vs_total_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['loan_status'] == "Fully Paid") & (self.df['total_payment'] < self.df['loan_amount'])
        ]
        print(f"Fully Paid loans with insufficient total payment: {anomalies.shape[0]}")
        sample = anomalies[['id','member_id','loan_status','loan_amount', 'total_payment','installment','last_payment_date']].head(sample_size)
        print("\nSample anomalies:\n", sample.to_string(index=False))
        return anomalies



    # Check whether fully paid loans have total payments less than or equal to the loan amount but interest rate > 0
    def status_vs_extra_payment(self, sample_size=5):
        anomalies = self.df[
            (self.df['loan_status'] == "Fully Paid") & (self.df['total_payment'] <= self.df['loan_amount']) & (self.df['int_rate'] > 0)
        ].copy()

        anomalies['payment_vs_principal'] = anomalies['total_payment'] - anomalies['loan_amount']
        print(f"Fully Paid loans with total_payment <= loan_amount and int_rate > 0: {len(anomalies)}")

        sample = anomalies[['id', 'member_id', 'loan_status', 'loan_amount', 'total_payment',
                'payment_vs_principal', 'installment', 'int_rate', 'issue_date', 'last_payment_date'
            ]].head(sample_size)

        print("\nSample anomalies:\n", sample.to_string(index=False))

        return anomalies


    # Check arrears for current loans based on expected payments and a tolerance level
    def current_loans_in_arrears(self, sample_size=5, tolerance=0.1):
        df = self.df[self.df['loan_status'] == "Current"].copy()
        df['loan_age_months'] = ((df['last_payment_date'] - df['issue_date']).dt.days / 30.4375)
        df['expected_paid_to_date'] = df['installment'] * df['loan_age_months']

        arrears = df[df['total_payment'] < df['expected_paid_to_date'] * (1 - tolerance)]
        print(f"Current loans in arrears: {len(arrears)}")
        sample = arrears[['id','member_id','loan_amount','total_payment','expected_paid_to_date','installment','issue_date','last_payment_date']].head(sample_size)
        print("\nSample arrears:\n", sample.to_string(index=False))
        return arrears
