import pandas as pd

# Sample data
data = {
    'Study_Hours': [2, 4, 5, 1, 6, 7, 3, 8, 5, 2],
    'Attendance_Rate': [50, 70, 80, 40, 90, 95, 60, 100, 85, 55],
    'Previous_Score': [45, 60, 65, 30, 75, 85, 50, 90, 70, 40],
    'Result': ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)
