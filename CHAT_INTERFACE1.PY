import streamlit as st
import random
import time
from app import *
import os
import re
import pandas as pd
import random 

st.set_page_config(page_title="Chatbot",layout="centered",initial_sidebar_state="expanded")

booking_id =  ['5AJ73850','5AJ88850','3BJ73850','9AJ73850','5AJ75550','2CJ73850','5AJ88880','4ZJ73850','5AJ79950','9JJ73850']

st.markdown("<h1 style='text-align: center;'>Restaurant bot 🤖</h1>", unsafe_allow_html=True)


chat_history  = ''
def f(df):
    st.data_editor(
        df,
        column_config={
            "command": "Item",
            "rating": st.column_config.NumberColumn(
                "rating",
                help="How much do you like this command (1-5)?",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
            ),
            "calories": "calories",
            "cost":"cost"
        },
        hide_index=True,
    )

with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Menu</h1>", unsafe_allow_html=True)
    for i in os.listdir('Menu'):
        df = pd.read_csv('Menu/'+i)
        if 'Desserts' in i:
            st.title(':rainbow[**' + i.split('.')[0]+'**] 🍰')
        elif  'Beverages' in i:
            st.title(':rainbow[**' + i.split('.')[0]+'**] 🍷')
        elif 'NonVeg' in i:
            st.title(':rainbow[**' + i.split('.')[0]+'**] 🍗')
        else:
            st.title(':rainbow[**' + i.split('.')[0]+'**]')
        f(df)
    





def response_generator(prompt,chat_history):
    Num_seats = os.getenv('NUM_SEATS')
    response = user_input(prompt,chat_history,Num_seats)
    return response['output_text']

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("What's up?"):
    num = 0
    if 'book' in prompt.lower() and 'seats' in prompt.lower():
        num = re.findall(r'\d+',prompt)
        if int(os.getenv("NUM_SEATS"))>int(num[0]):
            os.environ['NUM_SEATS']= str(int(os.getenv("NUM_SEATS"))-int(num[0]))
            print('NUM_SEATS',os.getenv("NUM_SEATS"),type(os.getenv("NUM_SEATS")))
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if num==0:
            st.write(response :=response_generator(prompt,chat_history))
        else:
            st.write(response :=response_generator(prompt,chat_history)+ '    Your Booking ID is '+ random.choice(booking_id))
    st.session_state.messages.append({"role": "assistant", "content": response})  
    chat_history += f"""User: {prompt}\nBot: {response}\n"""
    print(chat_history)  