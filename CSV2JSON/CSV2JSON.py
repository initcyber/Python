# CSV to JSON and Vice Versa

import csv
import json


# CSV to JSON
def csv_to_json(csv_file_path):
    """Converts a CSV file to JSON format"""
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    json_data = json.dumps(data, indent=4)
    return json_data

# JSON to CSV
def json_to_csv(json_data, csv_file_path):
    """Converts JSON data to CSV format and saves it to a CSV file"""
    data = json.loads(json_data)
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data[0].keys())
        for row in data:
            csv_writer.writerow(row.values())


# Ask User CSV2JSON or JSON2CSV
user_input = input("Enter 'C' for CSV2JSON or 'J' for 'JSON2CSV': ").upper()

# Convert CSV to JSON
if user_input == 'C':
    csv_file_path = input("Enter the CSV file path: ")
    json_data = csv_to_json(csv_file_path)
    json_file_path = input("Enter the JSON file path: ")
    with open(json_file_path, 'w') as file:
        file.write(json_data)

# Convert JSON to CSV
elif user_input == 'J':
    json_file_path = input("Enter the JSON file path: ")
    csv_file_path = input("Enter the CSV file path: ")
    with open(json_file_path, 'r') as file:
        json_data = file.read()
    json_to_csv(json_data, csv_file_path)

else:
    print("Invalid input. Please enter 'C' for CSV2JSON or 'J' for 'JSON2CSV'.")