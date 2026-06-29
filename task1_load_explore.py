import pandas as pd

# Load dataset
df = pd.read_csv("ai_learning_lab.csv")

# Explore dataset
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:", df.columns.tolist())

print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:", df.duplicated().sum())

print("\nValue counts for 'topic':")
print(df['topic'].value_counts())

print("\nValue counts for 'attendance':")
print(df['attendance'].value_counts())
