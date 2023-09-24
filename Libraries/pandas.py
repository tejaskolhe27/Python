
import pandas as pd
df1=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
df2=pd.read_table('http://bit.ly/movieusers',sep='|',header=None);


print(df1.columns)
print(df1["order_id"])
df1.rename(columns=({'choice_description':"choice"}),inplace=True)

df2.columns=["Sr No","Age","Gender","Job","Salary"]
print(df2.columns)
print(df2["Gender"])


print(df1.head()) #it will print first 5 lines
print(df2.tail()) #it will print last 5 lines

print(df1.info())
print(df2.info())

print(type(df2))
print(type(df1['choice']))

df3= df1[['quantity','choice']]
print(df1.iloc[1])
print(df1.iloc[2:7,1:4])

df1["newitem_price"]=df1['item_price'].map(lambda x:x.replace("$","0"))
df1["newitem_price"]=df1['newitem_price'].astype('float')
df1['discount_value']=df1['newitem_price'].map(lambda x:x*0.85)
df1['discount_value1']=df1['newitem_price']*0.85

#delete the column
df1.pop('discount_value1')

df1.drop(['newitem_price'],axis=1,inplace=True)

df2.drop([2,4],axis=0,inplace=True)

print(df1[df1['discount_value']>15])

index_num=df1[df1['discount_value']>17].index
df1.drop(index_num,axis=0,inplace=True)

print(df1.shape)
