# CSV Column Expansion

This Python script is designed to expand a CSV file's columns based on the values in the "MainFeatures" column. The script reads a CSV file named file.csv, located in the same directory as the script itself. It then processes the data in the "MainFeatures" column, splitting it by '|' and creating new columns based on the number of values found.

## Instructions

Requirements:
- Python 3.x
  
Setup:
- Ensure that the CSV file (file.csv) is in the same directory as the script.

Usage:
- Run the Python script. It will:
- Read the existing column names.
- Identify the "MainFeatures" column and split its values.
- Create new columns based on the number of split values.
- Update the CSV file by adding new columns and corresponding values.
- Print "Data Updated Successfully" upon completion.

Execution:
- Execute the script in a Python environment:
```bash
python script_name.py
```

## Output:
The script will modify the existing CSV file by adding new columns (if required) and populating them with relevant values from the "MainFeatures" column.

## Note:
Ensure that the CSV file has a header row with a column named "MainFeatures" that contains the values to be split into separate columns.
