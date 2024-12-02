import streamlit as st

def loginpage():

    st.title('Welcome to :red[Marvellous Models]')

    choice=st.selectbox('Login/Signup',['Login','Signup'])

    if choice=='Login':

        email=st.text_input('Email Address')
        password=st.text_input('Password',type='password')

        st.button('Login')

    else:

        email=st.text_input('Email Address')
        password=st.text_input('Password',type='password')
        Username=st.text_input('Enter your Unique Username')

        st.button('Create My Account')

