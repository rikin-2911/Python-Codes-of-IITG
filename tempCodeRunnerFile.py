import matplotlib.pyplot as plt     
import numpy as np   

np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data) 

plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Bos Plot')

plt.show()

