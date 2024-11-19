"""
Purpose: Exploring the relationship between two or more variables, identifying clusters and
outliers
● Philosophy: Highlighting the individual data points and their distribution, uncovering
correlations and associations
"""

import matplotlib.pyplot as plt     

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.scatter(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

plt.show()