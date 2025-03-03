# https://github.com/yourusername (commented-out URL, replace with your own)

# Import libraries
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt

# Ingest data from a local CSV file (Iris dataset)
df = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Manage different data types
# Ensure numeric columns are floats, and 'species' is a categorical type
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df[numeric_columns] = df[numeric_columns].astype(float)
df['species'] = df['species'].astype('category')

# Write your own function: Calculate average sepal length by species
def calculate_average_sepal_length(grouped_data):
    """Calculate the average sepal length for each species in the dataset."""
    return grouped_data['sepal_length'].mean()

# Use your function for data analysis
average_sepal_lengths = df.groupby('species').apply(calculate_average_sepal_length)
print("Average Sepal Length by Species:")
print(average_sepal_lengths)

# Visualize data: Bar chart of average sepal lengths by species
plt.figure(figsize=(8, 6))
average_sepal_lengths.plot(kind='bar')
plt.title("Average Sepal Length by Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.tight_layout()
plt.show()