import pandas as pd
import os
import time

process_data = []


def save_data(cpu_usage, memory_usage, process_list):
    entry = {
        'CPU (%)': cpu_usage,
        'Memory (%)': memory_usage,
        'Processes': len(process_list),
        'Time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    process_data.append(entry)


def export_data():
    if not process_data:
        return None, "No data available to export. Start monitoring first!"

    os.makedirs('data', exist_ok=True)
    file_path = "data/monitor_data.csv"

    pd.DataFrame(process_data).to_csv(file_path, index=False)
    return file_path, "Data exported successfully!"
