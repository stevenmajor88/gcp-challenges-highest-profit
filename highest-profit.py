
import csv

filename = 'data.csv'

# reading the data from the file

header = []
data = []

with open(filename) as csv_file:

	d = csv_file.readlines()

	for line in d:
		if len(header) == 0:
			header = line.split(',')
		else:
			data.append(line.split(','))

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