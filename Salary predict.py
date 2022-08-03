import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-southeast-1',
    aws_access_key_id='AKIAZEKCPVUWME6BWV64',
    aws_secret_access_key='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'
)

for bucket in s3.buckets.all():
    print(bucket.name)

import os
os.environ["AWS_DEFAULT_REGION"] = 'ap-southeast-1'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIAZEKCPVUWNYGXSDF6'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'E6QW9AkI9Nj5RwAB'

obj2018 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2018_Alc_Geography_xwalk.csv').get()
obj2019 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2019_Alc_xwalk_geography.csv').get()
obj2020 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2020_Alc_xwalk_geography.csv').get()
obj2021 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2021_Alc_xwalk_Geography.csv').get()
obj2022 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2022_Alc_xwalk_Geography.csv').get()
obj2023 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2023_Alc_Xwalk_geography.csv').get()

import pandas as pd
df_18=pd.read_csv(obj2018['Body'],index_col=1)
df_19=pd.read_csv(obj2019['Body'],index_col=1)
df_20=pd.read_csv(obj2020['Body'],index_col=1)
df_21=pd.read_csv(obj2021['Body'],index_col=1)
df_22=pd.read_csv(obj2022['Body'],index_col=1)
df_23=pd.read_csv(obj2023['Body'],index_col=1)


df_final = pd.concat([df_18,df_19,df_20,df_21,df_22,df_23])

df_final


print(df_final)

df_final.isnull().sum()
print(df_final)

print(df_final.isnull().sum())


df = df_final[["LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4","OES_SOCCODE","OES_SOCTITLE","ONETTITLE","AREA","AREANAME","STATEAB","COUNTYTOWNNAME","YEAR"]]
df = df_final.rename({"LEVEL1": "Level1_Salary","LEVEL2": "Level2_Salary","LEVEL3": "Level3_Salary","LEVEL4": "Level4_Salary","AVERAGE":"Average_Salary"}, axis=1)
print(df.head())

df = df[df["Level1_Salary"].notnull()]
print(df.head())

print(df.dtypes)

print(df.info())

df = df.dropna()
print(df.isnull().sum())

print(df["YEAR"].unique())

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1, figsize=(12, 7))
df.boxplot('Level1_Salary', 'STATE', ax=ax)
plt.suptitle('Salary_1 (US$) v STATE')
plt.title('')
plt.ylabel('Salary_1')
plt.xticks(rotation=90)
print(plt.show())

from sklearn.preprocessing import LabelEncoder
le_SOCCODE = LabelEncoder()
df['SOCCODE'] = le_SOCCODE.fit_transform(df['SOCCODE'])
print(df["SOCCODE"].unique())

le_OES_SOCCODE = LabelEncoder()
df['OES_SOCCODE'] = le_OES_SOCCODE.fit_transform(df['OES_SOCCODE'])
print(df["OES_SOCCODE"].unique())

le_OES_SOCTITLE = LabelEncoder()
df['OES_SOCTITLE'] = le_OES_SOCTITLE.fit_transform(df['OES_SOCTITLE'])
print(df["OES_SOCTITLE"].unique())

le_TRUNCONETCODE = LabelEncoder()
df['TRUNCONETCODE'] = le_TRUNCONETCODE.fit_transform(df['TRUNCONETCODE'])
print(df["TRUNCONETCODE"].unique())

le_ONETCODE = LabelEncoder()
df['ONETCODE'] = le_ONETCODE.fit_transform(df['ONETCODE'])
print(df["ONETCODE"].unique())

le_ONETTITLE = LabelEncoder()
df['ONETTITLE'] = le_ONETTITLE.fit_transform(df['ONETTITLE'])
print(df["ONETTITLE"].unique())

le_AREANAME = LabelEncoder()
df['AREANAME'] = le_AREANAME.fit_transform(df['AREANAME'])
print(df["AREANAME"].unique())

le_STATEAB = LabelEncoder()
df['STATEAB'] = le_STATEAB.fit_transform(df['STATEAB'])
print(df["STATEAB"].unique())

le_STATE = LabelEncoder()
df['STATE'] = le_STATE.fit_transform(df['STATE'])
print(df["STATE"].unique())

le_COUNTYTOWNNAME = LabelEncoder()
df['COUNTYTOWNNAME'] = le_COUNTYTOWNNAME.fit_transform(df['COUNTYTOWNNAME'])
print(df["COUNTYTOWNNAME"].unique())

print(df.head())

print(df.tail())

X = df.drop("Average_Salary", axis=1)
y = df["Average_Salary"]

from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
print(linear_reg.fit(X, y.values))

y_pred = linear_reg.predict(X)

from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
error = np.sqrt(mean_squared_error(y, y_pred))

print(error)

from sklearn.tree import DecisionTreeRegressor
dec_tree_reg = DecisionTreeRegressor(random_state=0)
dec_tree_reg.fit(X, y.values)

y_pred = dec_tree_reg.predict(X)

error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))

from sklearn.ensemble import RandomForestRegressor
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)

y_pred = random_forest_reg.predict(X)

error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))

from sklearn.model_selection import GridSearchCV

max_depth = [None, 2,4,6,8,10,12]
parameters = {"max_depth": max_depth}

regressor = DecisionTreeRegressor(random_state=0)
gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
gs.fit(X, y.values)

regressor = gs.best_estimator_

regressor.fit(X, y.values)
y_pred = regressor.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))

y_pred = regressor.predict(X)
print(y_pred)

import pickle
data = {"model": regressor, "le_SOCCODE": le_SOCCODE, "le_OES_SOCCODE": le_OES_SOCCODE,"le_OES_SOCTITLE": le_OES_SOCTITLE,"le_TRUNCONETCODE": le_TRUNCONETCODE,"le_ONETCODE": le_ONETCODE,"le_ONETTITLE": le_ONETTITLE,"le_AREANAME": le_AREANAME,"le_STATEAB": le_STATEAB,"le_STATE": le_STATE,"le_COUNTYTOWNNAME": le_COUNTYTOWNNAME}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)

regressor_loaded = data["model"]
le_SOCCODE = data["le_SOCCODE"]
le_OES_SOCCODE = data["le_OES_SOCCODE"]
le_OES_SOCTITLE = data["le_OES_SOCTITLE"]
le_TRUNCONETCODE = data["le_TRUNCONETCODE"]
le_ONETCODE = data["le_ONETCODE"]
le_ONETTITLE = data["le_ONETTITLE"]
le_AREANAME = data["le_AREANAME"]
le_STATEAB = data["le_STATEAB"]
le_STATE = data["le_STATE"]
le_COUNTYTOWNNAME = data["le_COUNTYTOWNNAME"]

y_pred = regressor_loaded.predict(X)
print(y_pred)
