import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import boto3 
import os

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-southeast-1',
    aws_access_key_id='AKIAZEKCPVUWME6BWV64',
    aws_secret_access_key='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'
)   

os.environ["AWS_DEFAULT_REGION"] = 'ap-southeast-1'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIAZEKCPVUWNYGXSDF6'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'E6QW9AkI9Nj5RwAB'

obj2018 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2018_Alc_Geography_xwalk.csv').get()
obj2019 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2019_Alc_xwalk_geography.csv').get()
obj2020 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2020_Alc_xwalk_geography.csv').get()
obj2021 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2021_Alc_xwalk_Geography.csv').get()
obj2022 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2022_Alc_xwalk_Geography.csv').get()
obj2023 = s3.Bucket('omsivaboolean').Object('FLC Data all Years/2023_Alc_Xwalk_geography.csv').get()

def load_data():
    df_18=pd.read_csv(obj2018['Body'],index_col=1)
    df_19=pd.read_csv(obj2019['Body'],index_col=1)
    df_20=pd.read_csv(obj2020['Body'],index_col=1)
    df_21=pd.read_csv(obj2021['Body'],index_col=1)
    df_22=pd.read_csv(obj2022['Body'],index_col=1)
    df_23=pd.read_csv(obj2023['Body'],index_col=1)

    df_final = pd.concat([df_18, df_19, df_20, df_21, df_22, df_23])
    df = df_final[
        ["LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "OES_SOCCODE", "OES_SOCTITLE", "ONETTITLE", "AREA", "AREANAME",
         "STATEAB", "COUNTYTOWNNAME", "YEAR"]]
    df = df_final.rename(
        {"LEVEL1": "Level1_Salary", "LEVEL2": "Level2_Salary", "LEVEL3": "Level3_Salary", "LEVEL4": "Level4_Salary",
         "AVERAGE": "Average_Salary"}, axis=1)
    df = df[df["Level1_Salary"].notnull()]
    df = df.dropna()
    return df

df=load_data()

def show_explore_page():
    st.title("Salary Predictor")

    st.write(
        """
    ### FLC Data 2018-2022
    """
    )

    data= df["STATE"].value_counts()

    fig1, ax1=plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%",shadow=True,startangle=90)
    ax1.axis("equal")

    st.write("""### Number of Data from Different States""")

    st.pyplot(fig1)

    st.write(
        """
        ### Mean Salary Based on state
        """
    )

    data = df.groupby(["STATE"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

