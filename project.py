import numpy as np
import pandas as pd
import seaborn as sns
from pandas import read_csv

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("source/persona.csv")

df.head()
df.info()
df.shape

df["SOURCE"].unique()
df["SOURCE"].value_counts()


df["PRICE"].unique()
df["PRICE"].value_counts()



df["COUNTRY"].value_counts()
df.groupby("COUNTRY").agg({"PRICE": "sum"})


df.groupby("SOURCE").agg({"PRICE": "count"})
df.groupby("SOURCE").agg({"PRICE": "mean"})

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending = False)
agg_df.reset_index(inplace = True)

# Yaş kategorilerini tanımlayın
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim:
labels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

# AGE_CAT sütununu oluşturun
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins = bins, labels= labels)

agg_df["customer_level_based"] = agg_df[["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].agg(lambda x: "_".join(x).upper(), axis = 1)

agg_df = agg_df[["customer_level_based", "PRICE"]]

agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})

agg_df = agg_df.reset_index()

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels = ["D", "C", "B", "A"])
agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user]

new_user1 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user1]














