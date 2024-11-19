"""
● Purpose: Visualizing the distribution of a single variable, identifying patterns and clusters
● Philosophy: Revealing the underlying frequency or probability distribution of a dataset,
highlighting the spread and concentration of data
"""
import matplotlib.pyplot as plt  
import numpy as np  

data = np.random.randn(1000)

plt.hist(data, bins = 30)

plt.xlabel('value')
plt.ylabel('Frequency')
plt.title('Histogram')

plt.show()