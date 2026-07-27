import matplotlib.pyplot as plt

# sample data
hours = [1, 2, 3, 4, 5, 6]
scores = [20, 30, 35, 50, 65, 80]

print("Generating Line Chart...")
# line chart
plt.figure(figsize=(6, 4))
plt.plot(hours, scores, marker='o', color='blue')
plt.title("Study Hours vs Scores")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.grid(True)
plt.savefig("line_chart.png")
print("Saved line_chart.png")
plt.close()




# bar chart
subjects = ["Math", "Science", "English", "History"]
marks = [78, 85, 72, 90]

print("Generating Bar Chart...")
plt.figure(figsize=(6, 4))
plt.bar(subjects, marks, color='green')
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("bar_chart.png")
print("Saved bar_chart.png")
plt.close()

# scatter plot
x = [1, 2, 3, 4, 5, 6]
y = [15, 25, 35, 45, 55, 65]

print("Generating Scatter Plot...")
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.savefig("scatter_plot.png")
print("Saved scatter_plot.png")
plt.close()

print("All plots generated successfully!")