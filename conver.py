import json
import csv

# Load the JSON data from the file
with open('final.json', 'r') as json_file:
    data = json.load(json_file)

# Define the CSV file name
csv_filename = 'output.csv'

# Open the CSV file for writing
with open(csv_filename, 'w', newline='') as csv_file:
    if isinstance(data, dict):
        # If JSON data is a dictionary, convert it to a list with one item
        data = [data]

    # Collect all unique field names
    fieldnames = set()
    for item in data:
        fieldnames.update(item.keys())
    fieldnames = list(fieldnames)

    # Create a CSV writer object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in data:
        writer.writerow(row)

print(f'CSV file "{csv_filename}" has been created successfully!')