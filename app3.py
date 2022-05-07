import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import plotly.express as px

def app():
    
    st.title('Travel Advisory')
    from_state = st.selectbox(
     'From Where are you going to travel',
     tuple(['A & N ISLANDS', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM',
            'BIHAR', 'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU',
            'DELHI UT', 'GOA', 'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH',
            'JAMMU & KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'LAKSHADWEEP',
            'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM',
            'NAGALAND', 'ODISHA', 'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM',
            'TAMIL NADU', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND', 'WEST BENGAL']))
    
    st.write('You selected:', from_state)
    to_state = st.selectbox(
     'From Where are you going to travel',
     tuple(['A & N ISLANDS', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM',
            'BIHAR', 'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU',
            'DELHI UT', 'GOA', 'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH',
            'JAMMU & KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'LAKSHADWEEP',
            'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM',
            'NAGALAND', 'ODISHA', 'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM',
            'TAMIL NADU', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND']))
    
    st.write('You selected:', to_state)
    suggestions={'MURDER':'Keep objects of self defence with you in public. Be prepared to defend yourself at all times. Remember emergency numbers. Do not engage the attackers unless it is absolutely unavoidable.  ',
            'RAPE':'Travel in well-lit, well-traveled areas. If possible, walk in pairs. Walk facing traffic. Plan your route ahead of time. Know your neighborhood - be aware of nearby businesses, their hours of operation and their locations. Avoid shortcuts, bushy areas, and alleyways. Dress for ease of movement.',
            'KIDNAPPING':'Don’t discuss your family with strangers. Do proper checks before employing workers. Don’t get too close to a stranger. Keep emergency numbers ready',
            'DACOITY':'During late night hours, request a stop by asking the driver to let you off anywhere along the route, even if it is not a designated stop. Use well-lit and busy stops whenever possible. If you’re getting off at a little-used stop, try to arrange for a friend to meet with you. When riding the bus or waiting at a bus stop stay alert, and don’t doze off.',
            'ROBBERY':' Carry your bag in front of you. Gentlemen, carry your wallet in your front pocket.',
             'FRAUD':'Pay the safest way. Guard your personal information. Don’t believe promises of easy money. Check money notes carefully',
            }
    data_url = "01_District_wise_crimes_committed_Merge_IPC_Till_2013.csv"
    mergedata=pd.read_csv(data_url)
    population_url = "State_population.csv"
    statepopulation=pd.read_csv(population_url)
    statepopulation['Population (2011 Census)[11]']=statepopulation['Population (2011 Census)[11]'].str.replace(',','')
    N=5
    crime_types=list(mergedata.columns[3:-1])
    fig, ax = plt.subplots(figsize=(15,40),nrows=11)
    i=int(0)
    for crime_type in crime_types:
        from_data=mergedata.loc[mergedata['STATE/UT']==from_state]
        to_data=mergedata.loc[mergedata['STATE/UT']==to_state]
        fd=int(statepopulation[statepopulation['STATE/UT']==from_state]['Population (2011 Census)[11]'])
        td=int(statepopulation[statepopulation['STATE/UT']==to_state]['Population (2011 Census)[11]'])
        from_data[crime_type]=from_data[crime_type].apply(lambda i: i/fd)
        from_data.index=list(from_data['YEAR'])
        to_data.index=list(to_data['YEAR'])
        to_data[crime_type]=to_data[crime_type].apply(lambda i: i/td)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        from_data[crime_type].plot(kind='line',y='TOTAL IPC CRIMES',ax=ax[i])
        to_data[crime_type].plot(kind='line',y='TOTAL IPC CRIMES',ax=ax[i],color='red')
        ax[i].set_title('Graph based on '+crime_type)
        # plt.xticks(list(from_data['YEAR']))
        ax[i].set_ylabel("Crime/Population")
        ax[i].legend(['from','to'])
        # ax[i].set_xlabel("Year")
        plt.show()
        i+=1
        # st.write(from_data)
        next_from_year=from_data.tail(N)[crime_type].sum()/N
        next_to_year=to_data.tail(N)[crime_type].sum()/N
        st.write(from_state, ' next year possible '+crime_type+' value is :',next_from_year)
        st.write(to_state,' next year possible '+crime_type+' value is :',next_to_year)
        if(next_to_year>next_from_year):
            st.write(crime_type+' On ' +to_state+' is more than your from state')
            if(crime_type in suggestions):
                st.write(suggestions[crime_type])
    st.pyplot(fig)
                
    
    