import pandas as pd

# Load the dataset
df = pd.read_csv("ai_learning_lab.csv")

# Print the shape of the dataset
print(df.shape)

# Print the first 5 rows
print(df.head())

# Print all column names
print(df.columns.tolist())

# Print data types using .info()
df.info()

# Print missing value count for each column
print(df.isnull().sum())

# Print the number of duplicate rows
print(df.duplicated().sum())

# Print value counts of the topic column
print(df["topic"].value_counts())

# Print value counts of the attendance column
print(df["attendance"].value_counts())
