import xlsxwriter

# Step 1: Read the input file and parse the sizes
file_sizes = []

with open('sizes.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(': ')
        if len(parts) == 2:
            size = int(parts[1])
            file_sizes.append(size)

# Step 2: Create a histogram of the file sizes
size_histogram = {}

for size in file_sizes:
    if size in size_histogram:
        size_histogram[size] += 1
    else:
        size_histogram[size] = 1

# Step 3: Write the histogram to an Excel file
workbook = xlsxwriter.Workbook('./file_size_histogram.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'File Size')
worksheet.write('B1', 'Count')

row = 1
for size, count in size_histogram.items():
    worksheet.write(row, 0, size)
    worksheet.write(row, 1, count)
    row += 1

workbook.close()