import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import plotly.express as px
# import plotly.express as px

data = pd.read_csv("F:\\Streamlit_learn\\Data Science_ Crime Analysis _ Safety recommendation - Dataset\\01_District_wise_crimes_committed_IPC_2001_2012.csv")
total = data[(data["DISTRICT"] == "TOTAL")]
tamilnadu = total[(total["STATE/UT"] == "TAMIL NADU")]

fig, (ax_0, ax_1) = plt.subplots(figsize=(15,10), nrows=2)
sns.pointplot(data=tamilnadu, x="YEAR", y="MURDER", ax=ax_0, color="blue");
sns.pointplot(data=tamilnadu, x="YEAR", y="KIDNAPPING & ABDUCTION", ax=ax_1, color="red");
ax_0.set_title("Murder and Kidnapping cases in Tamil Nadu", size=20);
sns.set_theme(style="dark")
st.pyplot(fig)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
DATA_URL="F:\\Streamlit_learn\\geoJson\\india\\district\\india_district.geojson"
df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='active cases',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(50,1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)
# progress_bar.empty()
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it justcauses a plain
# rerun.
st.button("Re-run")