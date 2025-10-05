import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

size=np.arange(8,13)

price=np.arange(300,550,50)

#scatter,title,xlabel,ylabel,xlim,ylim,show
plt.scatter(size,price)
plt.title("size vs price")
plt.xlabel("size")
plt.ylabel("price")
plt.xlim(8,13)
plt.ylim(300,550)
plt.show()