import seaborn as s
import matplotlib.pyplot as plt
import numpy as np
tips = s.load_dataset('tips')
# print(tips.head())
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
# there are many cetagorical cols
# s.barplot(x = 'sex',y = 'total_bill',data = tips)
# plt.show()
# barplot will show the average of the total_bill by sex
# ie avg total_bill by males and avg total_bill by females

# it is avg by default but you  can change it
# s.barplot(x = 'sex', y = 'total_bill',data= tips, estimator= np.sum)
# plt.show()
# now it will show the total sum of the money spent by male and female
# or you can pass any other functions like standard daviation as np.std


# s.countplot(x= 'sex',data = tips)
# plt.show()
# this simply counts the number of male and female in the dataset


# s.boxplot(x = 'day',y = 'total_bill',data= tips)
# plt.show()
# it visualize data as a boxplot


# s.stripplot(x = 'sex',y = 'total_bill', data= tips,jitter = True,hue='day',split=True)
# plt.show()
# another for visualization
# on adding hue it will show according to the days
# different color points for different days
# to get more info here
# by using split it will show for all days at differnt location
# it can give male at thursday, male at fri, male at sun then female at and so on

s.factorplot(x= 'sex',y = 'tip',data=tips,kind = 'bar')
plt.show()
# this is a genearl form
# kind means the type of plot you want
