import seaborn as s
import matplotlib.pyplot as plt
tips = s.load_dataset('tips')
# print(tips.head())
#  total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
# this is a dataset of people leaving a tip. you can study this dataset by looking at these cols
# we can draw a distplot ie graph for a single col
# we will draw it for the tip
# s.distplot(tips['tip'])
# this plot looks like a histogram
# it is a KDE kernal density estimation
# plt.show() this line is added just to show the graph
# to remove the line KDE in the graph
# s.distplot(tips['tip'],kde=False,bins=1)
# plt.show() you can clearly see that mostly the tip is between 2 and 4 this is actual data visualization
# highest plots in the histograms is between 2 and 4 so most pople give tip between 2 and 4
# bin is put there to get extra info out of it
# bin = number means the number of plots you want in the histogram how many vertical bars you want this can be done to
#  get more specific info out of it
#

# next is the joint plot
# this is actually the combination of 2 dist plots
# this is done when you want to compare 2 cols of a dataset to each other
# eg if you want to companre total bills and tip from the dataset
# maybe you want to know how to relate to each other
# then
# s.jointplot('total_bill','tip',tips)
# total bill and tip are the 2 col names and tips is the dataset

# plt.show()
# from the jointplot you can clearly see that when people have more bill they give more tip

# you by default get a scatter plot from jointplot but you can get any other plot that you want
# this is done by passing the third arg kind which is default to scatter

# s.jointplot('total_bill','tip',tips,kind='hex')
# plt.show()
# or kind = 'kde' or maybe kind = 'reg' etc

# pairplot is the next topic
# it is a quick way to visualize the data
# pairplot plots grpah(scatter plots by default) between everypair of cols
# ie it will plot a graph between total_bill,tip,size all the numeric cols
# total_bill vs tip, total_bill vs size, total_bill vs total_bill and so on
# s.pairplot(tips)
# you just have to pass the dataset and it will automatically plot graphs
# plt.show()
# size vs size etc same cols will be shown by histogram
# for cetagorical variables you have to pass the third arg hue
# s.pairplot(tips,hue='sex')
# plt.show()
# the col sex is passed which means that this will also be visualized in the plots


# rugplot
# s.rugplot(tips['tip'])
# plt.show()