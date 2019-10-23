#survival.py that bins how many people survive (Survived == 1) for each gender in 10-year blocks
#Count survivors by age and gender in these blocks:
	#

import matplotlib.pyplot as plt
import pylab 
import pandas as pd
import numpy as np 

#setting the dataframe
df = pd.read_csv("train.csv")

#not enough data to be useful > drop 
df.drop(["Cabin"], axis=1, inplace=True)
df = df[df.Survived != '0']

#df.drop(["Survived"==0])
#drop any NA values 
df.dropna(inplace=True)

#make a bar chart
#plt.bar()

#graph_by_duration = df.pivot(index='address', columns='used_at', values='active_seconds')
width = 2
fig = plt.figure()
ax = plt.plot()
plt.ylabel("Count (Survived)")
plt.xlabel('Age')
plt.xlim([0, 100])
plt.ylim([0, 60])
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],["0","10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
fig.suptitle('Survival by Age and Gender', fontsize=12)


#Filtering for groups: 0 <= age < 10, 10 <= age < 20, …, 90 <= age < 100
#10
m_10 = len(df[(df["Sex"] == "male") & (df["Age"] >= 0) & (df["Age"] < 10) & (df["Survived"]== 1)])
f_10 = len(df[(df["Sex"] == "female") & (df["Age"] >= 0) & (df["Age"] < 10) & (df["Survived"]== 1)])
m_10plt = plt.bar(10 - 1, m_10, width, label='male')
m_10plt[0].set_color('b')
f_10plt = plt.bar(10 + 2, f_10, width, label='female')
f_10plt[0].set_color('darkorange')

#20
m_20= len(df[(df["Sex"] == "male") & (df["Age"] >= 10) & (df["Age"] < 20) & (df["Survived"]== 1)])
f_20 = len(df[(df["Sex"] == "female") & (df["Age"] >= 10) & (df["Age"] < 20) & (df["Survived"]== 1)])
m_20plt = plt.bar(20 - 1, m_20, width)
m_20plt[0].set_color('b')
f_20plt = plt.bar(20 + 1, f_20, width)
f_20plt[0].set_color('darkorange')

#30
m_30= len(df[(df["Sex"] == "male") & (df["Age"] >= 20) & (df["Age"] < 30) & (df["Survived"]== 1)])
f_30 = len(df[(df["Sex"] == "female") & (df["Age"] >= 20) & (df["Age"] < 30) & (df["Survived"]== 1)])
m_30plt = plt.bar(30 - 1, m_30, width)
m_30plt[0].set_color('b')
f_30plt = plt.bar(30 + 1, f_30, width)
f_30plt[0].set_color('darkorange')

#40
m_40= len(df[(df["Sex"] == "male") & (df["Age"] >= 30) & (df["Age"] < 40) & (df["Survived"]== 1)])
f_40 = len(df[(df["Sex"] == "female") & (df["Age"] >= 30) & (df["Age"] < 40) & (df["Survived"]== 1)])
m_40plt = plt.bar(40 - 1, m_40, width)
m_40plt[0].set_color('b')
f_40plt = plt.bar(40 + 1, f_40, width)
f_40plt[0].set_color('darkorange')

#50
m_50= len(df[(df["Sex"] == "male") & (df["Age"] >= 40) & (df["Age"] < 50) & (df["Survived"]== 1)])
f_50 = len(df[(df["Sex"] == "female") & (df["Age"] >= 40) & (df["Age"] < 50) & (df["Survived"]== 1)])
m_50plt = plt.bar(50 - 1, m_50, width)
m_50plt[0].set_color('b')
f_50plt = plt.bar(50 + 1, f_50, width)
f_50plt[0].set_color('darkorange')

#60
m_60= len(df[(df["Sex"] == "male") & (df["Age"] >= 50) & (df["Age"] < 60) & (df["Survived"]== 1)])
f_60 = len(df[(df["Sex"] == "female") & (df["Age"] >= 50) & (df["Age"] < 60) & (df["Survived"]== 1)])
m_60plt = plt.bar(60 - 1, m_60, width)
m_60plt[0].set_color('b')
f_60plt = plt.bar(60 + 1, f_60, width)
f_60plt[0].set_color('darkorange')

#70
m_70= len(df[(df["Sex"] == "male") & (df["Age"] >= 60) & (df["Age"] < 70) & (df["Survived"]== 1)])
f_70 = len(df[(df["Sex"] == "female") & (df["Age"] >= 60) & (df["Age"] < 70) & (df["Survived"]== 1)])
m_70plt = plt.bar(70 - 1, m_70, width)
m_70plt[0].set_color('b')
f_70plt = plt.bar(70 + 1, f_70, width)
f_70plt[0].set_color('darkorange')

#80
m_80= len(df[(df["Sex"] == "male") & (df["Age"] >= 70) & (df["Age"] < 80) & (df["Survived"]== 1)])
f_80 = len(df[(df["Sex"] == "female") & (df["Age"] >= 70) & (df["Age"] < 80) & (df["Survived"]== 1)])
m_80plt = plt.bar(80 - 1, m_80, width)
m_80plt[0].set_color('b')
f_80plt = plt.bar(80 + 1, f_80, width)
f_80plt[0].set_color('darkorange')

#90
m_90= len(df[(df["Sex"] == "male") & (df["Age"] >= 80) & (df["Age"] < 90) & (df["Survived"]== 1)])
f_90 = len(df[(df["Sex"] == "female") & (df["Age"] >= 80) & (df["Age"] < 90) & (df["Survived"]== 1)])
m_90plt = plt.bar(90 - 1, m_90, width)
m_90plt[0].set_color('b')
f_90plt = plt.bar(90 + 1, f_90, width)
f_90plt[0].set_color('darkorange')

#checking bucket entries
#print("bucket:", str(m_90))
#100
m_100= len(df[(df["Sex"] == "male") & (df["Age"] >= 90) & (df["Age"] < 100) & (df["Survived"]== 1)])
f_100 = len(df[(df["Sex"] == "female") & (df["Age"] >= 90) & (df["Age"] < 100) & (df["Survived"]== 1)])
m_100plt = plt.bar(100 - 1, m_100, width)
m_100plt[0].set_color('b')
f_100plt = plt.bar(100 + 1, f_100, width)
f_100plt[0].set_color('darkorange')

#creating the legend
pylab.legend(loc='upper right')



#show the bar chart
plt.show()

