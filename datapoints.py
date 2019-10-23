#datapoints > 2 x 2 plot showing how SibSp and Parch vary by age for both genders

#test subplots

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train.csv")

#not enough data to be useful > drop 
df.drop(["Cabin"], axis=1, inplace=True)

#drop any NA values 
df.dropna(inplace=True)

parch_female_age = df.loc[df["Sex"] == "female"]["Age"]
parch_female = df.loc[df["Sex"] == "female"]["Parch"]
parch_male = df.loc[df["Sex"] == "male"]["Parch"] 
parch_male_age = df.loc[df["Sex"] == "male"]["Age"]
sibsp_female = df.loc[df["Sex"] == "female"]["SibSp"]
sibsp_female_age = df.loc[df["Sex"] == "female"]["Age"]
sibsp_male = df.loc[df["Sex"] == "male"]["SibSp"]
sibsp_male_age = df.loc[df["Sex"] == "male"]["Age"]
#Label graphs
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6,6))


#Draw with blue data points 
ax[0,0].plot(sibsp_male_age, sibsp_male, "bo")
ax[0,1].plot(sibsp_female_age, sibsp_female, "bo")
ax[1,0].plot(parch_male_age, parch_male, "bo")
ax[1,1].plot(parch_female_age, parch_female, "bo")

ax[0,0].set_title("Male SibSp")
ax[0,1].set_title("Female SibSp")
ax[1,0].set_title("Male Parch")
ax[1,1].set_title("Female Parch")
ax[0,0].set_ylabel("# of Parents/Children")
ax[0,1].set_ylabel("# of Parents/Children")
ax[1,0].set_ylabel("# of Siblings/Spouses")
ax[1,1].set_ylabel("# of Siblings/Spouses")

#Create half inch of space 
plt.subplots_adjust(wspace = 0.5)
plt.subplots_adjust(hspace = 0.5)

plt.show()