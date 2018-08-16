import matplotlib.pyplot as plt
import matplotlib as pt
import numpy as np
a = [1,2,3] #this will give lineraly spaced 10 numbers from 0 to 5
b = [2,4,6]
# plt.plot(a,b)
# # plt.show()
# # shows the grpah of a and b
# plt.xlabel('this is a')
# plt.ylabel('this is b')
# plt.title('this is the title')
# plt.show()

# fig = plt.figure()
# axes = fig.add_axes([0,0,0,0])
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('titile')
# axes.plot(a,b)
# plt.show()
#0,0,0,0 are the axis

# plt.plot(a,b)
# plt.plot(b,a)
# plt.show()
#
# fig1 = plt.figure(figsize=(10,8)) #figsize means size of the plot, 10 is the width in inches and 8 is the height in inches
# ax = fig1.add_axes([0.1,0.1,0.8,0.8])#these numbers tell the location of the graph in the plot while figsize is telling us the
# # size of the graph
# ax.set_xlabel('no of classes')
# ax.set_ylabel('no of students')
# ax.set_title('student vs class')
# ax.plot(a,b,label = 'this is the a and b')
# ax.plot(b,a,label = 'this is the b and a')
# if you want to plot 2 lines together on a graph, the label will tell at the top of the graph which line
# represent  what
# plt.show()
# fig2 = plt.figure()
# ax1 = fig2.add_axes([0.1,0.1,0.8,0.8])
# ax2 = fig2.add_axes([0.2,0.5,0.4,0.3])
# ax1.set_xlabel('x of ax1')
# ax1.set_ylabel('y of ax1')
# ax1.set_title('title')
# do the same for ax2 as well


# add axes takes 4 arguments whic tells us the loaction of the fraph on the plot
# the first number is the left, the second one is bottom, then width and the height of the axes.
# ax1.plot(a,b)
# ax2.plot(b,a)
# plt.show() it will now show two graphs on the same plot but both will be at differemt location due to diffeent location
# in this way you can create maultiple plots on the same graph


# creating subplots
# fig,ax = plt.subplots(nrows=2,ncols=3)
# this will create row x cols no of graphs the plot will be created and the plot will have 2 rows and 3 cols and all of 6 grpahs

# the ax there is an object of the axes for all the 6 graph created so you have to iterate through it
# for cax in ax:
#     cax.plot(a,b)
#     or you can use the index to set the graph in each graph in the plot;

# ax[0].plot(x,y)
# ax[0].set_xlabels('')
# ax[1].plot(y,x)
# title etc can be set to any of the 6 graphs
# and so on
# plt.show()


# use plt.tight_layout() to make sure there is no overlapping between graphs etc

# saving a figure as an image
# fig = plt.figure()
# ax = fig.add_axes([.1,.1,.8,.8])
# ax.plot(a,b,label= 'this is a and b')
# ax.plot(b,a,label = 'this is b and a')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_title('TiTLE')
# ax.legend()
# you can also set the location of this legend
# add ax.legend() to show the labels and these labels help to understand the graph when there are multiple plots
# labels will show which line represent what
# fig.savefig('testPlot.png')
# plt.show()
