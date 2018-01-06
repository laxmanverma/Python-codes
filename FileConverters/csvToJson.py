import csv
import json

#Read CSV File
file = 'csv_file_name.csv'
json_file = 'output_file_name.json'

def read_csv(file, json_file, format='pretty'):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
        else:
            f.write(json.dumps(data))

#read_csv(file,json_file,'dump')
read_csv(file,json_file)
