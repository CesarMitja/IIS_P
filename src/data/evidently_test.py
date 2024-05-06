import os
import pandas as pd
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

def analyze_drift(current_data_path, reference_data_path):
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
    report = os.path.join(project_root, 'reports','data_drift.html')
    current_data = pd.read_csv(current_data_path)
    reference_data = pd.read_csv(reference_data_path)

    data_drift_report = Dashboard(tabs=[DataDriftTab()])
    data_drift_report.calculate(reference_data, current_data)
    data_drift_report.save(report)

if __name__ == "__main__":
    analyze_drift('data/processed/current_data.csv', 'data/processed/reference_dataset.csv')