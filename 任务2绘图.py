import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
path='8月地铁人流量数据.xlsx'
#path=’9月地铁人流量数据.xlsx’
#path=’10月地铁人流量数据.xlsx’
#path=’11月地铁人流量数据.xlsx’
data=pd.read_excel(path)
zd=data.iloc[:,1]
zd=zd.unique()
j=1
rs=[]
for i in zd:
    tb=data.loc[data['Ad']==i,['day','C']].sort_values('day')
    j=tb.iloc[:,1]
    rs.append(j)
    j=j+1
x=np.arange(1,len(tb.iloc[:,0])+1)
plt.figure(figsize=(15,10))
plt.rcParams['font.sans-serif']='SimHei'
plt.plot(x,rs[0], color='pink',marker='*')
plt.plot(x,rs[1],color='yellowgreen',marker='*')
plt.plot(x,rs[2],color='red',marker='*')
plt.plot(x,rs[3],color='purple',marker='*')
plt.plot(x,rs[4],color='orange',marker='*')
plt.plot(x,rs[5],color='black',marker='*')
plt.plot(x,rs[6],color='blue',marker='*')

plt.plot(x,rs[7],color='cyan',marker='*')
plt.plot(x,rs[8],color='darkred',marker='*')
plt.plot(x,rs[9],color='deepskyblue',marker='*')
plt.plot(x,rs[10],color='green',marker='*')
plt.plot(x,rs[11],color='khaki',marker='*')
plt.plot(x,rs[12],color='maroon',marker='*')
plt.plot(x,rs[13],color='tomato',marker='*')
plt.plot(x,rs[14],color='sandybrown',marker='*')
plt.plot(x,rs[15],color='silver',marker='*')
plt.plot(x,rs[16],color='peru',marker='*')
plt.plot(x,rs[17],color='mediumvioletred',marker='*')
plt.plot(x,rs[18],color='lightgray',marker='*')
plt.plot(x,rs[19],color='chocolate',marker='*')     
plt.xlabel('日期')
plt.ylabel('人流量')

plt.title('8月地铁人流量走势图')
# plt.title('9月地铁人流量走势图')
# plt.title('10月地铁人流量走势图')
# plt.title('11月地铁人流量走势图')
plt.legend(sorted(zd)) ##站点标签
###plt.legend(['127','157','123','155','159','125','121','129','153','147','151','149','133','135','145','143','131','141','137','139'])
plt.xticks([1,5,10,15,20,25,30],tb['day'].values[[0,4,9,14,19,24,29]],rotation=45)
plt.savefig('myfigure1')
#plt.savefig('myfigure2')
#plt.savefig('myfigure3')
#plt.savefig('myfigure4')

path='9月地铁人流量数据.xlsx'
data=pd.read_excel(path)
zd=data.iloc[:,1]
zd=zd.unique()
j=1
rs=[]
for i in zd:
    tb=data.loc[data['Ad']==i,['day','C']].sort_values('day')
    j=tb.iloc[:,1]
    rs.append(j)
    j=j+1
x=np.arange(1,len(tb.iloc[:,0])+1)
plt.figure(figsize=(15,10))
plt.rcParams['font.sans-serif']='SimHei'
plt.plot(x,rs[0], color='pink',marker='*')
plt.plot(x,rs[1],color='yellowgreen',marker='*')
plt.plot(x,rs[2],color='red',marker='*')
plt.plot(x,rs[3],color='purple',marker='*')
plt.plot(x,rs[4],color='orange',marker='*')
plt.plot(x,rs[5],color='black',marker='*')
plt.plot(x,rs[6],color='blue',marker='*')

plt.plot(x,rs[7],color='cyan',marker='*')
plt.plot(x,rs[8],color='darkred',marker='*')
plt.plot(x,rs[9],color='deepskyblue',marker='*')
plt.plot(x,rs[10],color='green',marker='*')
plt.plot(x,rs[11],color='khaki',marker='*')
plt.plot(x,rs[12],color='maroon',marker='*')
plt.plot(x,rs[13],color='tomato',marker='*')
plt.plot(x,rs[14],color='sandybrown',marker='*')
plt.plot(x,rs[15],color='silver',marker='*')
plt.plot(x,rs[16],color='peru',marker='*')
plt.plot(x,rs[17],color='mediumvioletred',marker='*')
plt.plot(x,rs[18],color='lightgray',marker='*')
plt.plot(x,rs[19],color='chocolate',marker='*')           
plt.xlabel('日期')
plt.ylabel('人流量')

plt.title('9月地铁人流量走势图')
plt.legend(sorted(zd)) ##站点标签
plt.xticks([1,5,10,15,20,25,30],tb['day'].values[[0,4,9,14,19,24,29]],rotation=45)
plt.savefig('myfigure2')

path='10月地铁人流量数据.xlsx'
data=pd.read_excel(path)
zd=data.iloc[:,1]
zd=zd.unique()
j=1
rs=[]
for i in zd:
    tb=data.loc[data['Ad']==i,['day','C']].sort_values('day')
    j=tb.iloc[:,1]
    rs.append(j)
    j=j+1
x=np.arange(1,len(tb.iloc[:,0])+1)
plt.figure(figsize=(15,10))
plt.rcParams['font.sans-serif']='SimHei'
plt.plot(x,rs[0], color='pink',marker='*')
plt.plot(x,rs[1],color='yellowgreen',marker='*')
plt.plot(x,rs[2],color='red',marker='*')
plt.plot(x,rs[3],color='purple',marker='*')
plt.plot(x,rs[4],color='orange',marker='*')
plt.plot(x,rs[5],color='black',marker='*')
plt.plot(x,rs[6],color='blue',marker='*')

plt.plot(x,rs[7],color='cyan',marker='*')
plt.plot(x,rs[8],color='darkred',marker='*')
plt.plot(x,rs[9],color='deepskyblue',marker='*')
plt.plot(x,rs[10],color='green',marker='*')
plt.plot(x,rs[11],color='khaki',marker='*')
plt.plot(x,rs[12],color='maroon',marker='*')
plt.plot(x,rs[13],color='tomato',marker='*')
plt.plot(x,rs[14],color='sandybrown',marker='*')
plt.plot(x,rs[15],color='silver',marker='*')
plt.plot(x,rs[16],color='peru',marker='*')
plt.plot(x,rs[17],color='mediumvioletred',marker='*')
plt.plot(x,rs[18],color='lightgray',marker='*')
plt.plot(x,rs[19],color='chocolate',marker='*')           
plt.xlabel('日期')
plt.ylabel('人流量')

plt.title('10月地铁人流量走势图')
plt.legend(sorted(zd)) ##站点标签
plt.xticks([1,5,10,15,20,25,30],tb['day'].values[[0,4,9,14,19,24,29]],rotation=45)
plt.savefig('myfigure3')

path='11月地铁人流量数据.xlsx'
data=pd.read_excel(path)
zd=data.iloc[:,1]
zd=zd.unique()
j=1
rs=[]
for i in zd:
    tb=data.loc[data['Ad']==i,['day','C']].sort_values('day')
    j=tb.iloc[:,1]
    rs.append(j)
    j=j+1
x=np.arange(1,len(tb.iloc[:,0])+1)
plt.figure(figsize=(15,10))
plt.rcParams['font.sans-serif']='SimHei'
plt.plot(x,rs[0], color='pink',marker='*')
plt.plot(x,rs[1],color='yellowgreen',marker='*')
plt.plot(x,rs[2],color='red',marker='*')
plt.plot(x,rs[3],color='purple',marker='*')
plt.plot(x,rs[4],color='orange',marker='*')
plt.plot(x,rs[5],color='black',marker='*')
plt.plot(x,rs[6],color='blue',marker='*')

plt.plot(x,rs[7],color='cyan',marker='*')
plt.plot(x,rs[8],color='darkred',marker='*')
plt.plot(x,rs[9],color='deepskyblue',marker='*')
plt.plot(x,rs[10],color='green',marker='*')
plt.plot(x,rs[11],color='khaki',marker='*')
plt.plot(x,rs[12],color='maroon',marker='*')
plt.plot(x,rs[13],color='tomato',marker='*')
plt.plot(x,rs[14],color='sandybrown',marker='*')
plt.plot(x,rs[15],color='silver',marker='*')
plt.plot(x,rs[16],color='peru',marker='*')
plt.plot(x,rs[17],color='mediumvioletred',marker='*')
plt.plot(x,rs[18],color='lightgray',marker='*')
plt.plot(x,rs[19],color='chocolate',marker='*')           
plt.xlabel('日期')
plt.ylabel('人流量')

plt.title('11月地铁人流量走势图')
plt.legend(sorted(zd)) ##站点标签
plt.xticks([1,5,10,15,20,25,30],tb['day'].values[[0,4,9,14,19,24,29]],rotation=45)
plt.savefig('myfigure4')
