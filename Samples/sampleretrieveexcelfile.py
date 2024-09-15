import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'sampleexcel.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Extract account_number and account_description columns
account_numbers = df['account_number']
account_descriptions = df['account_description']

# Generate SQL update statements
for number, description in zip(account_numbers, account_descriptions):
    sql_statement = f"UPDATE account_table SET account_description='{description}' WHERE account_number='{number}';"
    print(sql_statement)
