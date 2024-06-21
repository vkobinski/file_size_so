# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = './file_size_histogram.xlsx'  # Update this path if the file name or path is different

# Load the Excel file
df = pd.read_excel(file_path)

# Extract the two columns
column1 = df["File Size"]  

# Plot the histogram
plt.figure(figsize=(10, 6))

plt.hist(column1, bins=20, alpha=0.5, label='Column1')  # Adjust bins and labels as needed

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Two Columns')
plt.legend()

# Show the plot
plt.savefig('books_read.png')