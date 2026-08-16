import numpy as np

marks = np.array([
    78, 85, 92, 67, 54,
    89, 73, 95, 61, 48
])

print("===== STUDENT PERFORMANCE =====")

print("Marks:", marks)

print("\nTotal Marks:", np.sum(marks))

print("Average Marks:", np.mean(marks))

print("Median Marks:", np.median(marks))

print("Highest Marks:", np.max(marks))

print("Lowest Marks:", np.min(marks))

print("Standard Deviation:", np.std(marks))

print("\nSorted Marks:")
print(np.sort(marks))

passed = marks[marks >= 40]

failed = marks[marks < 40]

print("\nPassed Students:", passed)

print("Failed Students:", failed)

print("\nNumber Passed:", len(passed))

print("Number Failed:", len(failed))