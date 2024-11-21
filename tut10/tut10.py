import streamlit as st
import pandas as pd
import numpy as np
import logging
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_grade(input_df):
    logging.info("Processing grades started.")
    try:
        max_marks = input_df.iloc[0, 2:6].astype(float)
        weightage = input_df.iloc[1, 2:6].astype(float)

        def calculate_grand_total(row):
            return (
                (row['Mid Sem'] / max_marks['Mid Sem']) * weightage['Mid Sem'] +
                (row['Endsem'] / max_marks['Endsem']) * weightage['Endsem'] +
                (row['Quiz 1'] / max_marks['Quiz 1']) * weightage['Quiz 1'] +
                (row['Quiz 2'] / max_marks['Quiz 2']) * weightage['Quiz 2']
            )

        students_with_names = input_df[input_df['Name'].notna()].copy()
        students_without_names = input_df[input_df['Name'].isna()].copy()

        students_with_names.loc[:, 'Grand Total/100'] = students_with_names.apply(calculate_grand_total, axis=1)

        students_with_names = students_with_names.sort_values(by='Grand Total/100', ascending=False).reset_index(drop=True)

        def assign_grade_based_on_percentile(index, total_students):
            percentile = (index + 1) / total_students * 100
            if percentile <= 5:
                return 'AA'
            elif percentile <= 20:
                return 'AB'
            elif percentile <= 45:
                return 'BB'
            elif percentile <= 75:
                return 'BC'
            elif percentile <= 90:
                return 'CC'
            elif percentile <= 95:
                return 'CD'
            else:
                return 'DD'

        students_with_names.loc[:, 'Grade'] = students_with_names.index.to_series().apply(
            assign_grade_based_on_percentile, total_students=len(students_with_names)
        )

        final_df = pd.concat([students_without_names, students_with_names], ignore_index=True)

        first_three_rows = final_df.iloc[:2]
        remaining_rows = final_df.iloc[2:]
        remaining_rows = remaining_rows.sort_values(by='Roll').reset_index(drop=True)
        final_df2 = pd.concat([first_three_rows, remaining_rows], ignore_index=True)

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            final_df.to_excel(writer, sheet_name='Sorted_grade_wise', index=False)
            final_df2.to_excel(writer, sheet_name='Sorted_rollno_wise', index=False)

        logging.info("Processing grades completed successfully.")
        return output
    except Exception as e:
        logging.error(f"Error during grade processing: {e}")
        raise

st.title("Grade Processing App")
st.write("Upload an Excel file with grading information to generate the output with grades and statistics.")

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    try:
        input_data = pd.read_excel(uploaded_file, sheet_name='Sheet1')
        st.success("Input file loaded successfully.")
        logging.info("Input file loaded successfully.")

        output = process_grade(input_data)

        st.download_button(
            label="Download Output Excel File",
            data=output,
            file_name="processed_grades.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error("An error occurred while processing the file. Please ensure the format is correct.")
        logging.error(f"Exception: {e}")
