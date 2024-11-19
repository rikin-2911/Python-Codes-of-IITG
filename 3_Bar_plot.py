"""
● Purpose: Comparing discrete, categorical, or aggregated data points
● Philosophy: Emphasizing the magnitude and relative differences between distinct categories
or groups
"""

import matplotlib.pyplot as plt     

categories = ['A' 'B', 'C', 'D', 'E']
values = [2, 3, 3, 5, 4]

plt.bar(categories, values) 

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')

plt.show()

