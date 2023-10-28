# importing matplotlib for graph generation
import matplotlib.pyplot as plt

# Sample marks data for 15 students
marks = [1,9,4,6,8,19,10,13,17,2,4,15,20,7,9]

# Define the bins
bins = [1, 5, 10, 15, 20]

# Create the histogram
plt.hist(marks, bins=bins, edgecolor='k')

# Label the axes and set a title
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')
plt.title('Histogram of Student Marks')

# Show the histogram
plt.show()
