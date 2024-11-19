"""
● Purpose: Displaying trends, patterns, and relationships over time or continuous variables
● Philosophy: Emphasizing the continuity and progression of data points, revealing temporal
or sequential insights
"""

import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

plt.show()