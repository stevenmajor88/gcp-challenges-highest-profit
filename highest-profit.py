
# --- PART 1 ---

import csv
import re

filename = 'data.csv'

# reading the data from the file

data = list(csv.reader(open(filename)))
header = data.pop(0)

# first printed answer
print(len(data))


filtered_data = []
# removing non-numeric profit rows.

for row in data:
	if len(row) == 5:
		try:
			row[-1] = float(row[-1])
			filtered_data.append(row)
		except:
			# if non-numeric	
			continue

# second printed answer
print(len(filtered_data))


# --- PART 2 ---

import json

jsonFile = open('data2.json', 'w')

for row in filtered_data:

	row_data = {}
	for i in range(len(header)):
		row_data[header[i].strip()] = row[i]

	json.dump(row_data, jsonFile)
	jsonFile.write("\n")


jsonFile.close()

# printing top-20 records

filtered_data = sorted(filtered_data, key=lambda l:l[-1], reverse=True)

# third print answer
print("Top 20 records:")
print(','.join(header))

for i in range(20):
	print(filtered_data[i])