import matplotlib.pyplot as plt

marks = [55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()