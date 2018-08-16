import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('tips.csv')
# if you want to create the histogram of the first col
# df['total_bill'].hist()
# plt.show()

# df['tip'].hist()
# or df['tip'].plot(kind = 'hist') will do the same
# plt.show()

# df.plot.area()
# plt.show()

# df.plot.bar()
# plt.show()

# df.plot.scatter(x='total_bill',y='tip')
# plt.show()
# this shows total bill vs tip graph showing scatter plot

# df.plot.box()
# plt.show()


# you can also plot the kde of a col
# df['tip'].plot.kde()
# plt.show()
# or pass any other col