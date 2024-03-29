data_str = "5.0, 100, 5.5, 101, 6.0, 102:L10;5.0, 99, 5.5, 100, 6.0, 101:L20"

# Split the string into components based on ";"
major_components = data_str.split(";")

# Initialize a list to hold parsed numeric data and labels separately
numeric_data = []
labels = []

for component in major_components:
    # For each component, split further based on ":"
    num_data, label = component.split(":")
    # Split the numeric data by commas and convert to pairs of [value, measurement]
    num_data_pairs = [[float(num_data.split(", ")[i]), float(num_data.split(", ")[i+1])] for i in range(0, len(num_data.split(", ")), 2)]
    numeric_data.append(num_data_pairs)
    labels.append(label)

# Prepare the matrix structure
# Assuming all numeric data components have the same "x values" (e.g., 5.0, 5.5, 6.0)

# Extract the unique x values (first elements of the pairs) for row headers
x_values = [pair[0] for pair in numeric_data[0]]

# Prepare the matrix with x_values as the first column and subsequent columns for each label
matrix = [[x] + [None] * len(labels) for x in x_values]

# Fill in the matrix with the corresponding y values
for col_index, data_set in enumerate(numeric_data, start=1):
    for row_index, pair in enumerate(data_set):
        matrix[row_index][col_index] = pair[1]

# Combine labels into the header
header = ["X"] + labels

(matrix, header)
