import csv
# Load the CSV content into memory (read all rows)
rows = []
with open('customers.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    # Read and copy all rows into memory
    for row in csv_reader:
        rows.append(row)

# Search for the row and modify it
for row in rows:
    if row[0] != 'mohammad': continue

    # Write the modified data back to the CSV file
    row[2] = int(row[2]) + 100

# Open the file in 'w' mode, but this time write all rows back to the file
with open('customers.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)

    # Write the updated rows (including all rows, not just the modified one)
    csv_writer.writerows(rows)