# https://github.com/samimshs/PythonCodeSnippet

# I will not be able to use actual data from my actual work for obvious reasons. Here, I am using the most famous dataset for the purpose of this requirement.

# Requirement Number 1: Import libraries
# I am importing the warnings module to make sure any and all warnings that do not impact the code are ignored. I saw a couple of unnecessary warnings in the output. 
# Next, I am importing the data manipulation and data visualization libraries to work with the data.
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt

# Requirement Number 2: Ingest data from a CSV file (Iris dataset) hosted on Github
df = pd.read_csv('https://raw.githubusercontent.com/samimshs/PythonCodeSnippet/refs/heads/main/iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Requirement Number 3: Manage different data types
# Ensure numeric columns are floats, and 'species' is a categorical type
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df[numeric_columns] = df[numeric_columns].astype(float)
df['species'] = df['species'].astype('category')

# Requirement Number 3: Write your own function: Calculate average sepal length by species
def calculate_average_sepal_length(grouped_data):
    """Calculate the average sepal length for each species in the dataset."""
    return grouped_data['sepal_length'].mean()

# Requirement Number 4: Use your function for data analysis
average_sepal_lengths = df.groupby('species').apply(calculate_average_sepal_length)
print("Average Sepal Length by Species:")
print(average_sepal_lengths)

# Requirement Number 5: Visualize data: Bar chart of average sepal lengths by species
plt.figure(figsize=(8, 6))
average_sepal_lengths.plot(kind='bar')
plt.title("Average Sepal Length by Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.tight_layout()
plt.show()