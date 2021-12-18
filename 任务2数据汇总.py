import pandas as pd
import numpy as np

##二分法查找
## fun.py 函数包
def find_index(A):
    a0=int(A.iloc[0,0][8:10])   ##  第一天
    a2=int(A.iloc[len(A)-1,0][8:10])    ##最后一天
    tA=A   ## 赋值
    while 1:    
      I1=int(len(tA)/2)-1    ##数据折半
      I2=I1+1
      t0=int(tA.iloc[I1,0][8:10])
      ##i1的日期
      t2=int(tA.iloc[I2,0][8:10])  ##i2的日期
      if t2!=t0:    ##判断i1和i2的日期
         r=(tA.iloc[I1,0][:10],tA.index[I1])
         return r
         break
      if t2==t0 and t2==a0: 
          tA=tA.iloc[I2:,]   ##后半部分
      if t2==t0 and t2==a2:
          tA=tA.iloc[:I1+1,]  ###前半部分


name = '08'

A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[5])
S=pd.Series(A.iloc[:,0].values)  ##站点
Ad=S.unique()   ##去重  站点
reader=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',chunksize=100000,usecols=[6])

##提起1—30号日期
R=[] #每日数据的结束index
for A in reader:
    a0=int(A.iloc[0,0][8:10])
    a2=int(A.iloc[len(A)-1,0][8:10])
    if a0!=a2:
      r=find_index(A)
      R.append(r)

#八月数据的提取
A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[4,5])##指定列交易类型和站点
# A=pd.read_csv('acc_09_final.csv',sep=',',usecols=[4,5])##指定列交易类型和站点
# A=pd.read_csv('acc_10_final.csv',sep=',',usecols=[4,5])##指定列交易类型和站点
#A=pd.read_csv('acc_11_final.csv',sep=',',usecols=[4,5])##指定列交易类型和站点


A=A.values  #转矩阵
Ad_values=[]    #站点
day_values=[]  #日期
C1_values=[]  #进站数
C2_values=[]  #出站数
for Z in range(len(Ad)):   ##站点循坏
    for t in range(len(R)+1):  ##时间循环
        if t==0:
            data=A[:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]   ##站点
            I2=data[:,0]==21   ##交易类型
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t>0 and t<len(R):
            data=A[R[t-1][1]+1:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t==len(R):
            data=A[R[t-1][1]+1:,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append('2015-08-31')##根据不同月份取最后一天数据
            Ad_values.append(Ad[Z])

## 9月
name = '09'

A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[5])
S=pd.Series(A.iloc[:,0].values)  ##站点
Ad=S.unique()   ##去重  站点
reader=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',chunksize=100000,usecols=[6])

##提起1—30号日期
R=[] #每日数据的结束index
for A in reader:
    a0=int(A.iloc[0,0][8:10])
    a2=int(A.iloc[len(A)-1,0][8:10])
    if a0!=a2:
      r=find_index(A)
      R.append(r)

#八月数据的提取
A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[4,5])##指定列交易类型和站点

A=A.values  #转矩阵

for Z in range(len(Ad)):   ##站点循坏
    for t in range(len(R)+1):  ##时间循环
        if t==0:
            data=A[:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]   ##站点
            I2=data[:,0]==21   ##交易类型
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t>0 and t<len(R):
            data=A[R[t-1][1]+1:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t==len(R):
            data=A[R[t-1][1]+1:,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append('2015-09-30')##根据不同月份取最后一天数据
            Ad_values.append(Ad[Z])


## 10月
name = '10'

A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[5])
S=pd.Series(A.iloc[:,0].values)  ##站点
Ad=S.unique()   ##去重  站点
reader=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',chunksize=100000,usecols=[6])

##提起1—30号日期
R=[] #每日数据的结束index
for A in reader:
    a0=int(A.iloc[0,0][8:10])
    a2=int(A.iloc[len(A)-1,0][8:10])
    if a0!=a2:
      r=find_index(A)
      R.append(r)

#八月数据的提取
A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[4,5])##指定列交易类型和站点

A=A.values  #转矩阵

for Z in range(len(Ad)):   ##站点循坏
    for t in range(len(R)+1):  ##时间循环
        if t==0:
            data=A[:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]   ##站点
            I2=data[:,0]==21   ##交易类型
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t>0 and t<len(R):
            data=A[R[t-1][1]+1:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t==len(R):
            data=A[R[t-1][1]+1:,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append('2015-08-31')##根据不同月份取最后一天数据
            Ad_values.append(Ad[Z])

## 11月
name = '11'

A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[5])
S=pd.Series(A.iloc[:,0].values)  ##站点
Ad=S.unique()   ##去重  站点
reader=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',chunksize=100000,usecols=[6])

##提起1—30号日期
R=[] #每日数据的结束index
for A in reader:
    a0=int(A.iloc[0,0][8:10])
    a2=int(A.iloc[len(A)-1,0][8:10])
    if a0!=a2:
      r=find_index(A)
      R.append(r)

#八月数据的提取
A=pd.read_csv('acc_{}_final.csv'.format(name),sep=',',usecols=[4,5])##指定列交易类型和站点

A=A.values  #转矩阵

for Z in range(len(Ad)):   ##站点循坏
    for t in range(len(R)+1):  ##时间循环
        if t==0:
            data=A[:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]   ##站点
            I2=data[:,0]==21   ##交易类型
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t>0 and t<len(R):
            data=A[R[t-1][1]+1:R[t][1]+1,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append(R[t][0])
            Ad_values.append(Ad[Z])
        if t==len(R):
            data=A[R[t-1][1]+1:,:]
            I1=data[:,1]==Ad[Z]
            I2=data[:,0]==21
            I3=data[:,0]==22
            C1_values.append(len(data[I1&I2,:]))
            C2_values.append(len(data[I1&I3,:]))
            day_values.append('2015-11-30')##根据不同月份取最后一天数据
            Ad_values.append(Ad[Z])



C_values = []
for i in range(len(C1_values)):
    C_values.append(C1_values[i]+C2_values[i])




D={'Ad':Ad_values,'day':day_values,'C1':C1_values,'C2':C2_values,'C':C_values}
Data=pd.DataFrame(D)
Data['day'] = pd.to_datetime(Data['day'])


df =   Data.groupby(Data['day']).sum()
del df['Ad']

df.to_csv('总测试数据（无Ad）.csv')

from chinese_calendar import is_workday

if_=[]
for index,row in Data.iterrows():
    if is_workday(row['day']):
        if_.append(0)
    else:
        if_.append(1)

Data['if'] = if_

Data_2 = Data[Data['if']==0]
del Data_2['if']

Data_2 = Data_2.groupby(Data_2['day']).sum()
Data_2.to_csv('总测试数据(非节假日非周末).csv')

import copy
Data_1 = copy.deepcopy(Data)

holiday = ['2015-10-1','2015-10-2','2015-10-3','2015-09-27']
for i in holiday:
    Data_1 = Data_1[~(Data_1['day']==i)]

Data_1 = Data_1.groupby(Data_1['day']).sum()
del Data_1['if'],Data_1['isWeekend']

Data_1.to_csv("总测试数据(非节假日).csv")

Data.to_csv('总数据测试(节假日).csv')

