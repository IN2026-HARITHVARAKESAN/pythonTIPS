import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


df =pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])

print(df.head()) # Print the first 5 rows of the DataFrame

df.plot(kind='scatter',x='a', y='b')

plt.show() # Displays the plot