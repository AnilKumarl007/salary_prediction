import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    a1.pie(data, labels=data.index, autopct="%1.1f%%",shadow=True,startangle=90)
    ax1.axis("equal")

    st.write("""### Number of Data from Different States""")

    st.pyplot(fig1)

    st.write(
        """
        ### Mean Salary Based on state
        """
    )

    data = df.groupby([STATE])["Salary"].mean(.sort_values(ascending=True)
    st.bar_chart(data)

st.write(
        """
        ### Mean Salary Changes for Years
        """
    )

    data = df.groupby(["YEAR"])["Salary"].mean(.sort_values(ascending=True)
    st.line_chart(data)
