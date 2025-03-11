import pickle
import pandas as pd
import streamlit as st

sih = pickle.load(open("hard_sih.pkl","rb"))

st.title("My new app")
selecting = st.selectbox("Select Your Poblem Statement",sih['Statement_id'])
Butt = st.button("Next")
# for i in selecting:
# for i in range(0,67):
if selecting:
  index=sih[sih['Statement_id']==selecting].index[0]
  info = sih.iloc[index]
  st.table(info)
 

# for i in range(0,67):
#  if Butt:
#     index=sih[sih['Statement_id']==selecting].index[0]
#     info = sih.iloc[index+i]
#     st.table(info)
st.write("List")
st.data_editor(sih)
