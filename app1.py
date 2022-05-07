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
    st.title('APP1')
    st.write('Welcome to app1')
    data = pd.read_csv("F:\\Streamlit_learn\\Data Science_ Crime Analysis _ Safety recommendation - Dataset\\01_District_wise_crimes_committed_IPC_2001_2012.csv")
    total = data[(data["DISTRICT"] == "TOTAL")]
    tamilnadu = total[(total["STATE/UT"] == "TAMIL NADU")]
    
    fig, (ax_0, ax_1) = plt.subplots(figsize=(15,10), nrows=2)
    sns.pointplot(data=tamilnadu, x="YEAR", y="MURDER", ax=ax_0, color="blue");
    sns.pointplot(data=tamilnadu, x="YEAR", y="KIDNAPPING & ABDUCTION", ax=ax_1, color="red");
    ax_0.set_title("Murder and Kidnapping cases in Tamil Nadu", size=20);
    sns.set_theme(style="dark")
    st.pyplot(fig)