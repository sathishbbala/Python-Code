import matplotlib.pyplot as plt


# Data for the plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
yhigh = [31, 32, 32, 31, 30, 30, 30, 29, 28, 29, 29, 28, 28, 28, 27, 27, 28, 27, 28, 28, 28, 28, 28, 28, 28, 27, 27, 26, 27, 28]
ylow = [26, 27, 27, 26, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 22, 22, 23]

# fig = plt.figure()
fig,axes = plt.subplots(1, 2, figsize=(15, 7))   # Create two side-by-side subplots for low and high temperatures
axes[0].plot(x,ylow,color='blue',ls='--')
axes[0].set_xlabel('Daily')
axes[0].set_ylabel('Low Temp C')
axes[0].set_title('Low Temperature Chennai Nov 2025')
axes[1].plot(x,yhigh,color='red',ls='-.')
axes[1].set_xlabel('Daily')
axes[1].set_ylabel('High Temp C')
axes[1].set_title('High Temperature Chennai Nov 2025')

plt.show()