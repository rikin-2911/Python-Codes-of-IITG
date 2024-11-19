"""
● Purpose: Displaying the proportional composition or relative sizes of categorical data
● Philosophy: Emphasizing the relative contribution or share of each category within the
whole, providing a clear snapshot of the data
"""

import matplotlib.pyplot as plt     
import numpy as np   

data = np.random.rand(10, 10)

plt.imshow(data, cmap = 'hot')

plt.colorbar()

plt.title('Heatmap with Color Bar')

plt.show()

