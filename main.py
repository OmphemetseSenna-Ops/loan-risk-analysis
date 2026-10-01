from src.data_understanding_and_profiling import DataProfiler
from src.data_quality_alert_visuals import DataQualityVisualizer
from src.preprocessing import Preprocessor
from src.eda import EDA
from src.anomalies.anomaly_detector import AnomalyDetector
from src.anomalies.anomaly_and_data_quality import RiskAnalysis

if __name__ == "__main__":
    profiler = DataProfiler()
    visualizer = DataQualityVisualizer()
    preprocessor = Preprocessor()
    eda = EDA()
    detector = AnomalyDetector()
    risk_analysis = RiskAnalysis()

    # ## Display dataset overview
    # profiler.preview_data()
    # profiler.get_summary()
    # profiler.get_shape()
    # profiler.get_data_types()

    # ## Data Quality Checks
    # profiler.missing_summary()
    # profiler.duplicates()

    # ## Column Profiling
    # profiler.get_categorical_columns()
    # profiler.get_numeric_columns()
    # profiler.categorical_encoding_overview()

    # ## Preprocessing
    # fill_nulls_of_emp_title = preprocessor.replace_missing_with_unknown("emp_title")
    # preprocessor.save_processed()

    ## EDA
    # eda.dataset_overview()
    # eda.numeric_summary()
    # eda.correlation_heatmap()
    # cat_summary = eda.categorical_summary()
    # print("\nCategorical Summary:\n", cat_summary)
    # eda.date_summary()
    # eda.target_distribution(target_col="loan_status")

    # ## Anomaly Detection
    # numeric_outliers = detector.numeric_outliers("annual_income")
    # categorical_anomalies = detector.categorical_anomalies("home_ownership")
    # date_anomalies = detector.date_anomalies("issue_date")

    ### Risk Analysis
    risk_analysis.loan_ids_shared_by_members(sample_size=5)
    risk_analysis.duplicate_member_loans(sample_size=5)
    risk_analysis.duplicate_loan_ids(sample_size=5)

    risk_analysis.invalid_loan_amounts(sample_size=5)
    risk_analysis.invalid_annual_income(sample_size=5)
    risk_analysis.invalid_interest_rates(sample_size=5)

    risk_analysis.suspicious_dti(sample_size=5)
    risk_analysis.invalid_installments(sample_size=5)
    risk_analysis.invalid_total_payments(sample_size=5)
    risk_analysis.invalid_date_sequence(sample_size=5)

    risk_analysis.next_payment_before_last_payment(sample_size=5)
    risk_analysis.status_vs_next_payment(sample_size=5)
    risk_analysis.fully_paid_without_next_payment(sample_size=5)
    risk_analysis.status_vs_total_payment(sample_size=5)
    risk_analysis.status_vs_extra_payment(sample_size=5)
    risk_analysis.current_loans_in_arrears(sample_size=5)

    risk_analysis.active_loans_without_next_payment(sample_size=5)


    # risk_analysis.installment_consistency()
    # risk_analysis.dti_check()



    

    ## Visualizations
    # visualizer.missing_visualization()
    # visualizer.missing_barplot()
