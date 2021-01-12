#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.size"] = 15
plt.rcParams["figure.figsize"] = (8, 6)


# In[2]:


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open(r'C:\Users\pnu\Desktop\3.Bigdata_Analysis\Hadoop,Spark(window)\Hadoop_Spark-window-\Kafka\Work\samsung.txt').read()
    lines = graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line) > 1:
            x,y= line.split(',')
            print(x,y)
            xs.append(x)
            ys.append(y)

    print("---------")
    ax1.clear()
    ax1.plot(xs,ys)
    plt.xlabel('날짜')
    plt.ylabel('삼성 종가')
    plt.title('삼성 종가 라인 차트')
    plt.xticks(rotation=45)

ani = animation.FuncAnimation(fig, animate, interval=3000)
plt.show()

