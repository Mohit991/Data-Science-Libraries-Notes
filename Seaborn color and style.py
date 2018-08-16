import seaborn as s
import matplotlib.pyplot as plt
tips = s.load_dataset('tips')
# print(tips.head())
s.set_style('darkgrid')#this is a style there are many more that you can explore
# plt.figure(figsize=(12,12)) you can use the same from the matplotlib

s.set_context('poster')#for what you are creating the plot
s.countplot(x = 'sex',data=tips)
plt.show()