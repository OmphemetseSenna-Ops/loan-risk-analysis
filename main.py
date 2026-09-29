from src.data_understanding import DataProfiler
from src.data_quality_alert_visuals import DataQualityVisualizer

if __name__ == "__main__":
    file_path = "datasets/raw/financial_loan.xlsx"
    profiler = DataProfiler(file_path)
    visualizer = DataQualityVisualizer(file_path)

    ## Display dataset overview
    profiler.preview_data()
    profiler.get_summary()
    profiler.get_shape()
    profiler.get_data_types()

    ## Data Quality Checks
    profiler.missing_summary()
    profiler.duplicates()

    ## Column Profiling
    profiler.get_categorical_columns()
    profiler.get_numeric_columns()
    profiler.categorical_encoding_overview()













    ## Visualizations
    # visualizer.missing_visualization()
    # visualizer.missing_barplot()
