"""
● Purpose: Summarizing the distribution of a variable, identifying outliers and comparing
across groups
● Philosophy: Providing a compact and robust representation of the data's central tendency,
spread, and skewness, helping to identify and examine unusual observations
"""

import matplotlib.pyplot as plt     
import numpy as np   

np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data) 

plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Bos Plot')

plt.show()

