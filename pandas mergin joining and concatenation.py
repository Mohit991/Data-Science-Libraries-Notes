import pandas as pd
d1 = {'name':['a','b','c'],'age':[21,22,23]}
d2 = {'name':['d','e','f'],'age':[11,12,13]}
d3 = {'name':['g','h','i'],'age':[31,32,33]}
# these are 3 dictionary
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)
# how these 3 are dataframes
# now we can concetenate these dataframes
# this means combining the dataframes and for that their dimensions and col type must match otherwise error will be produced
print(pd.concat([df1,df2,df3]))
# this joins the rows from the dfs
#   age name
# 0   21    a
# 1   22    b
# 2   23    c
# 0   11    d
# 1   12    e
# 2   13    f
# 0   31    g
# 1   32    h
# 2   33    i
# the 3 dataframes have been joined together
print(pd.concat([df1,df2,df3],axis=1))
# this joins the cols from the dfs
#    age name  age name  age name
# 0   21    a   11    d   31    g
# 1   22    b   12    e   32    h
# 2   23    c   13    f   33    i
# first the first df then next df and so on


# merging is same as the merging in the sql
print(pd.merge(df1,df2))
# it will produce an empty result if there are no matching values betwwne the 2 dataframes

# print(d1)
# {'name': ['a', 'b', 'c'], 'age': [21, 22, 23]}
d4 = {'name': ['a', 'ba', 'ac'], 'age': [21, 22, 31]}
df4 = pd.DataFrame(d4)
# print(pd.merge(df1,df4,how='inner',on='name'))
#    age_x name  age_y
# 0     21    a     21

# this shows all the rows where name in the cols match
# also this can be any col like age etc
# how= '' shows how you want to merge inner left right or outer

# joining
# same as merge but this happens on the index rather than the cols