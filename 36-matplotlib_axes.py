import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [31, 32, 32, 31, 30, 30, 30, 29, 28, 29, 29, 28, 28, 28, 27, 27, 28, 27, 28, 28, 28, 28, 28, 28, 28, 27, 27, 26, 27, 28]

fig = plt.figure() # this creates a figure or canvas on which charts will be placed

#ax = fig.add_axes([0,0,1,1]) # adding a first chart 
# [left, bottom, width, height] using 0,0,1,1 uses the entire space and leaves no room for labels
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',lw=1, linestyle='-.', marker='o')  # lw is linewidth
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple Plot')

plt.show()
