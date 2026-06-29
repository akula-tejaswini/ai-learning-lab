import pandas as pd

# Load dataset safely
try:
    df = pd.read_csv("ai_learning_lab.csv", on_bad_lines="skip")  # skips malformed rows
except pd.errors.ParserError:
    df = pd.read_csv("ai_learning_lab.csv", sep=";", on_bad_lines="skip")  # try semicolon separator

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

if 'topic' in df.columns:
    print("\nValue counts for 'topic':")
    print(df['topic'].value_counts())

if 'attendance' in df.columns:
    print("\nValue counts for 'attendance':")
    print(df['attendance'].value_counts())
