"""This script generates a random DataFrame and creates a scatter plot of two of its columns."""
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

if __name__ == "__main__":
    df =pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])

    print(df.head())

    df.plot(kind='scatter',x='a', y='b')

    plt.show()