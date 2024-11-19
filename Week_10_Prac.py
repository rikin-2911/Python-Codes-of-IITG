import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,3,5,7,11]

#Creates a line plot
plt.plot(x,y, marker = 'o', linestyle = '-', color = 'blue', label = 'Data')

#Add labels to the axes
plt.xlabel('X-axis') # Add a label to the X-axis
plt.ylabel('Y-axis') # Add a label to the Y-axis

#Add a title to a line plot
plt.title('A line plot')

#Add a legend
plt.legend()

#Show a Plot
plt.show()

"""Creating a figure"""
fig = plt.figure(figsize = (4,4), facecolor = 'lightskyblue')
fig.suptitle('Rik-Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc = 'left')
plt.show()


"""Creating plots"""
#1
y = [1,2,3,4,5]
plt.plot(y)
plt.show()

#2
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y)
plt.show()

#3
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y, 'ro--')
plt.show()

#4
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y, color = 'blue', linestyle = 'dashed', linewidth = 2,\
         marker = 'o', markerfacecolor = 'red', markersize = '8', label = 'Data')
plt.show()

""" Two Ways to plot """
# Approach 1 : OOP style
x = np.linspace(0,2,100) #sample data

#we use '.pyplot.figure' to create the figure
fig, ax = plt.subplots(figsize = (5, 4))
ax.plot(x, x, label = "Linear")
ax.plot(x, x ** 2, label = 'Quadratic')
ax.plot(x, x ** 3, label = 'Cubic')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_title("Simple Plot")
ax.legend()
plt.show()

# Approac 2 : Non-OOP style
