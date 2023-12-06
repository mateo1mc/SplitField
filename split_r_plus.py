import os
import csv

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File name
file_name = 'file.csv'

# Construct the full path to the CSV file
file_path = os.path.join(script_dir, file_name)

# Open the CSV file for reading and writing
with open(file_path, 'r+', newline='', encoding='utf8') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Get the existing column names
    fieldnames = reader.fieldnames

    # Create new column names based on the number of values in the "MainFeatures" column
    if 'MainFeatures' in fieldnames:
        # Create a list to hold the updated rows
        updated_rows = []

        # Iterate over the rows in the CSV file
        for row in reader:
            # Split the "MainFeatures" column into separate values
            values = row['MainFeatures'].split('|')

            if len(values) > 1:
                # Create new column names based on the number of values
                new_column_names = [f'bullet{i+1}' for i in range(len(values))]

            else:
                # If there's only one value, create a single new column named "bullet1"
                new_column_names = ['bullet1']

            # Add the new column names to the fieldnames list if they're not already present
            for name in new_column_names:
                if name not in fieldnames:
                    fieldnames.append(name)

            # Update the row with the new column values
            row.update(dict(zip(new_column_names, values)))

            # Append the updated row to the list
            updated_rows.append(row)

        # Truncate the file to the start position
        csvfile.seek(0)

        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the updated rows
        writer.writerows(updated_rows)

        # Truncate the file to the current position
        csvfile.truncate()

        # Print message after finish it
        print("Data Updated Successfully")
