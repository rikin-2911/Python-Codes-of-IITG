"""
● Purpose: Displaying the proportional composition or relative sizes of categorical data
● Philosophy: Emphasizing the relative contribution or share of each category within the
whole, providing a clear snapshot of the data
"""

import matplotlib.pyplot as plt  

labels = ['A', 'B', 'C', 'D']
sizes = [20, 30, 25, 25]

plt.pie(sizes, labels = labels, autopct = '%1.1f%%')

plt.title('Pie Chart')

plt.show()

