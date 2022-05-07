import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import plotly.express as px
# import plotly.express as px

def app():
    st.title('Forecasting')
    data_url = "F:\\Streamlit_learn\\plotting_app\\01_District_wise_crimes_committed_Merge_IPC_Till_2013.csv"
    mergedata=pd.read_csv(data_url)
    crime = st.selectbox(
     'Select Crime',
     tuple(['MURDER', 'RAPE', 'KIDNAPPING',
            'DACOITY', 'ROBBERY', 'RIOTS', 'FRAUD', 'HURT', 'AGAINST WOMEN',
            'NEGLIGENCE', 'OTHER', 'TOTAL IPC CRIMES']))
    
    st.write('You selected:', crime)
    state = st.selectbox(
     'State',
     tuple(['A & N ISLANDS', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM',
            'BIHAR', 'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU',
            'DELHI UT', 'GOA', 'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH',
            'JAMMU & KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'LAKSHADWEEP',
            'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM',
            'NAGALAND', 'ODISHA', 'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM',
            'TAMIL NADU', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND','WEST BENGAL']))
    
    st.write('You selected:', state)
    # state='ANDHRA PRADESH'
    # crime='RAPE'
    
    moving_data=list(mergedata.loc[mergedata['STATE/UT']==state][crime])
    curdata=mergedata.loc[mergedata['STATE/UT']==state][[crime,'YEAR']]
    for year in range(2014,2023):
        value=sum(moving_data[-5:])/5
        nowyear=[value,year]
        curdata=pd.concat([curdata,pd.DataFrame({crime:[value],'YEAR':[year]})],axis=0)
        moving_data.append(value)
    
    curdata.plot(x='YEAR',y=crime,kind='line')
    plt.show()
    st.pyplot()
    # st.write('Welcome to app1')
    # data = pd.read_csv("F:\\Streamlit_learn\\Data Science_ Crime Analysis _ Safety recommendation - Dataset\\01_District_wise_crimes_committed_IPC_2001_2012.csv")
    # total = data[(data["DISTRICT"] == "TOTAL")]
    # tamilnadu = total[(total["STATE/UT"] == "TAMIL NADU")]
    
    # fig, (ax_0, ax_1) = plt.subplots(figsize=(15,10), nrows=2)
    # sns.pointplot(data=tamilnadu, x="YEAR", y="MURDER", ax=ax_0, color="blue");
    # sns.pointplot(data=tamilnadu, x="YEAR", y="KIDNAPPING & ABDUCTION", ax=ax_1, color="red");
    # ax_0.set_title("Murder and Kidnapping cases in Tamil Nadu", size=20);
    # sns.set_theme(style="dark")
    # st.pyplot(fig)