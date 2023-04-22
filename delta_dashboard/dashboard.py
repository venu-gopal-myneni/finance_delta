import streamlit as st

import sys

sys.path.insert(0,"C:\\Users\\shenron\\projects\\finance_delta")
print(sys.path)
from delta_engine.equity import get_daily

st.title('Finance Delta')

# # USING FORMS
# with st.form("my_form"):
#     col1, col2, col3,col4 = st.columns(4)
#     with col1:
        
#         start_date = st.date_input(
#         "Start Date",)
#         st.write('Start date is:', start_date)

#     with col2:
#         end_date = st.date_input(
#         "End Date",)
#         st.write('End date is:', end_date)

#     with col3:
#         country = st.radio(
#         "Select a country",
#         ('USA', 'IND'))
#         st.write(f"You selected {country}")
#     with col4:
#         stock = st.radio("Select a stock",('MSFT','INFY'))
#         st.write(f"You selected {stock}")
    
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write(f"Submitted : {start_date},{end_date},{country},{stock}")

# st.write(f"Submitted : {start_date},{end_date},{country},{stock}")



# USING BUTTONS

col1, col2, col3,col4 = st.columns(4)
with col1:
    
    start_date = st.date_input(
    "Start Date",)
    st.write('Start date is:', start_date)

with col2:
    end_date = st.date_input(
    "End Date",)
    st.write('End date is:', end_date)

with col3:
    country = st.radio(
    "Select a country",
    ('USA', 'IND'))
    st.write(f"You selected {country}")
with col4:
    stock = st.radio("Select a stock",('MSFT','INFY'))
    st.write(f"You selected {stock}")

clicked = st.button("Get Chart")
if clicked:
    data =get_daily(start_date,end_date,stock,country)
    st.dataframe(data)