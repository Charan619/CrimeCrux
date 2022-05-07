import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import plotly.express as px

def app():
    
    st.title('Visulization')
    # st.write('Welcome to app2')
    option = st.selectbox(
     'Select the crime',
     tuple(['MURDER', 'RAPE', 'KIDNAPPING', 'DACOITY', 'ROBBERY', 'RIOTS',
            'FRAUD', 'HURT', 'AGAINST WOMEN', 'NEGLIGENCE', 'OTHER',
            'TOTAL IPC CRIMES']))

    st.write('You selected:', option)
    option2 = st.selectbox(
     'Select the year',
     tuple(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
            '2012', '2013','ALL']))

    st.write('You selected:', option2)
    data_url = "01_District_wise_crimes_committed_Merge_IPC_Till_2013.csv"
    d1=pd.read_csv(data_url)
    if(option2=='ALL'):
        d2=d1.groupby(by='STATE/UT').sum()
        d2=d2.drop('D & N HAVELI')
        d2.loc['TELENGANA']=d2.loc['ANDHRA PRADESH']
        df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
        d2.index=df['state']
        d2['state']=list(df['state'])
        
        df['active cases']=list(d2[option])
    else:
        df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
        d2=d1[d1['YEAR']==int(option2)]
        d2.index=df['state']
        d2['state']=list(df['state'])
        # d2=d2.drop('D & N HAVELI')
        # d2.loc['TELENGANA']=d2.loc['ANDHRA PRADESH']        
        df['active cases']=list(d2[option])
    # st.write(d2[option])
    df.rename(columns = {'active cases': 'Crimes'}, inplace = True)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Crimes',
        color_continuous_scale='Reds',
        title="Heatmap of Crimes"
    )
    
    fig.update_geos(fitbounds="locations", visible=False)
    
    st.plotly_chart(fig)