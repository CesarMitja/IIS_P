import pandas as pd
import os

def load_and_combine_data(data, data2):
    combined_data = pd.merge_asof(
        data.sort_values('index'), 
        data2.sort_values('index'), 
        left_on='index', 
        right_on='index',
        direction='nearest'
    )
    return combined_data

def add_average_column(data):
    data['AVG_subject'] = data[['STEM_subjects', 'H_subjects']].mean(axis=1)
    return data

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
    raw_data_path1 = os.path.join(project_root, 'data', 'raw','students.csv')
    raw_data_path2 = os.path.join(project_root, 'data', 'raw','students_scores.csv')
    data1 = pd.read_csv(raw_data_path1)
    data2 = pd.read_csv(raw_data_path2)
    processed_data_path = os.path.join(project_root, 'data', 'processed')
    
    combined_data = load_and_combine_data(data1,data2)
    combined_data = add_average_column(combined_data)
    combined_data.to_csv(os.path.join(processed_data_path, 'current_data.csv'))

if __name__ == "__main__":
    main()