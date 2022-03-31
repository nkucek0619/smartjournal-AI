# csv to jsonl
import csv
import json

reader = None
# open test.csv
with open('test.csv', 'r') as f:
    # read the file
    reader = csv.reader(f)

    # convert the data to a list
    data = list(reader)

final_data = []

# get the first row
first_row = data[0]

# loop through the data, after the first row
for row in data[1:]:
    # loop through the row
    temp = {}
    if len(row) < 2:
        continue
    for i in range(len(row)):
        # get the value
        value = row[i]
        # get the header
        header = first_row[i]
        # print the value
        temp[header] = value

    # add the temp to the final data
    final_data.append(temp)

# output to json file
with open('test.jsonl', 'w') as f:
    for item in final_data:
        f.write(json.dumps(item) + '\n')