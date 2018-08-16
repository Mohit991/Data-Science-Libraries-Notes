import pandas as pd
# group by is similiar to the group by in SQL
# use aggregate functions just like slq
data = {'company':['fb','fb','go','go','ma'],'person':['mohit','rohit','zohit','purohit','laila'],'sales':[220,440,100,450,500]}
df = pd.DataFrame(data)
# print(df)
#   company   person  sales
# 0      fb    mohit    220
# 1      fb    rohit    440
# 2      go    zohit    100
# 3      go  purohit    450
# 4      ma    laila    500
# now you can group by comapny as
bycom = df.groupby('company')
# now bycom is an object which contains the dataframe grouped by company names
# you can call a aggregate function on it to get the actual outputs
# when group by is used all the string cols are not used
# eg here person is  a string col so it will not be used for calculations
# print(bycom.mean())
#          sales
# company
# fb         330
# go         275
# ma         500
# shows the mean sales for each company
# print(bycom.sum())
#       sales
# company
# fb         660
# go         550
# ma         500
# shows the sum of all the sales for all companies
# or if you want for a perticular company
print(bycom.sum().loc['fb'])
# it prints the sum for the company named fb


# to do this all in one line we have
# print(df.groupby('company').sum())


# some other useful agg functions are:
# count, max, min, describe etc