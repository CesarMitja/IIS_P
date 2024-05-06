import pandas as pd
import os

def convert_dtypes(input_df, reference_df):
    for column in input_df.columns:
        if column in reference_df.columns:
            input_df[column] = input_df[column].astype(reference_df[column].dtype)
    return input_df

def validate_data(input_df, reference_df):
    if len(input_df.columns) != len(reference_df.columns):
        print(f"Nepravilno število stolpcev")
    else:
        print("Pravilno število stoplcev")


    reference_df.columns = input_df.columns

    if not all(input_df.columns == reference_df.columns):
        print("Napačna imena stolpcev")
        mismatches = [(input_col, ref_col) for input_col, ref_col in zip(input_df.columns, reference_df.columns) if input_col != ref_col]
        print("Napaka pri:", mismatches)
    else:
        print("Pravilna imena stolpcev")

    input_df = convert_dtypes(input_df, reference_df)

    mismatched_types = {}
    for col in input_df.columns:
        if input_df[col].dtype != reference_df[col].dtype:
            mismatched_types[col] = (input_df[col].dtype, reference_df[col].dtype)

    if mismatched_types:
        print("Podatkovni tipi so nepravilno")
    else:
        print("Podatkovni tipi so pravilni")

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
    data_path1 = os.path.join(project_root, 'data', 'processed', 'current_data.csv')
    input_df1 = pd.read_csv(data_path1)
    data_path2 = os.path.join(project_root, 'data', 'processed', 'current_data.csv')
    input_df2 = pd.read_csv(data_path2)
    validate_data(input_df1, input_df2)

if __name__ == "__main__":
    main()