import streamlit as st

# messages=[]

# def ask_question(question):
#     messages.append({'role':'user','content':question})
#     response=openai.chat.completions.create(
#         model='gpt-3.5-turbo',
#         messages=messages
#     )
#     print(response)
#     ChatGPT_reply=response.choices[0].message.content
#     print(ChatGPT_reply)
#     messages.append({'role':'assistant','content':ChatGPT_reply})

#     return ChatGPT_reply

# st.write(ask_question('Hello'))

def homepage():
    st.write('Welcome to Marvellous Models')
    # Add a page link to Google
    st.page_link("https://huggingface.co/", label="Hugging Face", icon="🤗")
    st.page_link("https://streamlit.io/", label="Streamlit", icon="👑")

