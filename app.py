#app.py
import app1
import app2
import app3
import streamlit as st
PAGES = {
    "Forecasting": app1,
    "Visualization": app2,
    "Travel Advisory": app3
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()