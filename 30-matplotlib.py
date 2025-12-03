import matplotlib.pyplot as plt


# Data for the plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
yhigh = [31, 32, 32, 31, 30, 30, 30, 29, 28, 29, 29, 28, 28, 28, 27, 27, 28, 27, 28, 28, 28, 28, 28, 28, 28, 27, 27, 26, 27, 28]
ylow = [26, 27, 27, 26, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 22, 22, 23]

# Create the plot
plt.scatter(x, yhigh, linestyle = 'dotted', color = 'r')
plt.scatter(x, ylow, linestyle = 'dotted', color = 'g')


# Add labels and a title
plt.xlabel("November 2025 - Daily")
plt.ylabel("Temperature in C")
plt.title("Simple Line Plot")

# Display the plot
plt.show()