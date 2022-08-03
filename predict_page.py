import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data= load_model()

regressor= data["model"]
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

def show_predict_page():
    st.title("Salary prediction")

    STATE =(
        'SOUTH CAROLINA',
        'NEW YORK',
        'WASHINGTON',
        'FLORIDA',
        'INDIANA',
        'TEXAS',
        'ARKANSAS',
        'OHIO',
        'KANSAS',
        'NEW JERSEY',
        'SOUTH DAKOTA',
        'ARIZONA',
        'OKLAHOMA',
        'ALABAMA',
        'HAWAII',
        'GEORGIA',
        'CALIFORNIA',
        'TENNESSEE',
        'VIRGINIA',
        'NORTH CAROLINA',
        'MICHIGAN',
        'DISTRICT OF COLUMBIA',
        'MARYLAND',
        'WEST VIRGINIA',
        'IOWA',
        'LOUISIANA',
        'KENTUCKY',
        'IDAHO',
        'MINNESOTA',
        'MISSISSIPPI',
        'WISCONSIN',
        'MISSOURI',
        'PENNSYLVANIA',
        'ILLINOIS',
        'Missouri',
        'Illinois',
        'Oregon',
        'California',
        'Delaware',
        'Maryland',
        'Utah',
        'Texas',
        'Puerto Rico',
        'Pennsylvania',
        'New Mexico',
        'Georgia',
        'Washington',
        'Florida',
        'Wisconsin',
        'Louisiana',
        'Arizona',
        'South Dakota',
        'Iowa',
        'Nebraska',
        'Indiana',
        'Michigan',
        'South Carolina',
        'Ohio',
        'Virginia',
        'New York',
        'Arkansas',
        'Kansas',
        'New Jersey',
        'West Virginia',
        'Kentucky',
        'Alabama',
        'Idaho',
        'Minnesota',
        'Mississippi',
        'Tennessee',
        'North Carolina',
        'Hawaii',
        'Rhode Island',
        'Colorado',
        'Connecticut',
        'Alaska',
        'Montana',
        'North Dakota',
    )

    YEAR = (
        '2018',
        '2018',
        '2020',
        '2021',
        '2022',
        '2023',
    )

    STATE = st.selectbox("Select Levels",Level1_Salary, Level2_Salary,Level3_Salary,Level4_Salary)

    YEAR= st.selectbox("Select Year",2018,2018,2020,2021,2022,2023)

    ok= st.button("Calculate Salary")
    if ok:
        X= np.array([[STATE,YEAR]])
        X[:,0] = le_STATE.transform(X[:,0])
        X=X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.3f}")