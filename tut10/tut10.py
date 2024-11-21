import pandas as pd

input_file_path = 'Input-1.xlsx'
input_df = pd.read_excel(input_file_path)

max_marks = input_df.iloc[0, 2:6].astype(float)
weightage = input_df.iloc[1, 2:6].astype(float)
def calculate_grand_total(row):
    return ((row['Mid Sem'] / max_marks['Mid Sem']) * weightage['Mid Sem'] +
            (row['Endsem'] / max_marks['Endsem']) * weightage['Endsem'] +
            (row['Quiz 1'] / max_marks['Quiz 1']) * weightage['Quiz 1'] +
            (row['Quiz 2'] / max_marks['Quiz 2']) * weightage['Quiz 2'])

students_with_names = input_df[input_df['Name'].notna()]
students_without_names = input_df[input_df['Name'].isna()]

students_with_names['Grand Total/100'] = students_with_names.apply(calculate_grand_total, axis=1)

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
    elif percentile <= 100:
        return 'DD'

students_with_names['Grade'] = students_with_names.index.to_series().apply(
    assign_grade_based_on_percentile, total_students=len(students_with_names)
)
final_df = pd.concat([students_without_names, students_with_names], ignore_index=True)

first_three_rows=final_df.iloc[:2];
remaining_rows=final_df.iloc[2:];
remaining_rows=remaining_rows.sort_values(by='Roll').reset_index(drop=True);

final_df2=pd.concat([first_three_rows,remaining_rows],ignore_index=True);

output_path = 'Output-1.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    final_df.to_excel(writer, sheet_name='Sorted_grade_wise', index=False)
    final_df2.to_excel(writer, sheet_name='Sorted_rollno_wise', index=False)
