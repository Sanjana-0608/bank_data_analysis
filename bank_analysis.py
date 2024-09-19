

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("inputs/bank.csv", sep=';')

print(data.head())

# Print some info
print("-"*50)
print(data.info())

# Describe the dataset
print("-"*50)
print(data.describe())

# Number of dirty rows in data
print("-"*50)
print(data.isnull().sum())


# Start of analysis
print("-"*50)
sns.countplot(x='y', data=data)
plt.title("Count Plot of Subscription Description")
plt.show()

# Start of analysis
print("-" * 50)
sns.countplot(x='y', data=data)
plt.title("Count Plot of Subscription Description")
plt.show()

# Analysis by Job
plt.figure(figsize=(12, 6))
sns.countplot(x='job', hue='y', data=data)
plt.xticks(rotation=45)
plt.title("Subscription by Job")
plt.show()

# Analysis by Age
plt.figure(figsize=(12, 6))
sns.countplot(x='age', hue='y', data=data)
plt.xticks(rotation=90)
plt.title("Subscription by Age")
plt.show()