import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("StudentsPerformance.csv")

print("=== First 5 Records ===")
print(data.head())

# Rename columns for easy use
data.rename(columns={
    'math score': 'Math',
    'reading score': 'Reading',
    'writing score': 'Writing'
}, inplace=True)

# Calculate total and average
data['Total'] = data[['Math', 'Reading', 'Writing']].sum(axis=1)
data['Average'] = data[['Math', 'Reading', 'Writing']].mean(axis=1)

print("\n=== Student Performance Summary ===")
print(data[['gender', 'Math', 'Reading', 'Writing', 'Total', 'Average']].head())

# Topper
topper = data.loc[data['Total'].idxmax()]
print("\n=== Top Performing Student ===")
print(topper)

# Subject-wise average
subject_avg = data[['Math', 'Reading', 'Writing']].mean()
print("\n=== Subject-wise Average Scores ===")
print(subject_avg)

# Visualization: Subject-wise average
subject_avg.plot(kind='bar')
plt.title("Subject-wise Average Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# Visualization: Gender vs Average Score
gender_avg = data.groupby('gender')['Average'].mean()
gender_avg.plot(kind='bar')
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()
