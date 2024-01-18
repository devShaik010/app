
import google.generativeai as genai
import streamlit as st
st.header('A LLM Model')

st.title('Ai ChatBot - genai  😎')
st.write('Created By Shaik Abrar 👩‍💻')

genai.configure(
    api_key='AIzaSyBx4XvQGoJliaAbndMaDAWTv_CX4V6KacY')
model = genai.GenerativeModel(
    model_name='gemini-pro')

def run(promt):
    if promt=="":
        promt = "How to write Prompt ?"
    response = model.generate_content(promt)
    return response

promt = st.text_input('🍀 Write Your Query here.',placeholder="Enter Prompt")
if st.button('Run'):
    response=run(promt)

    st.write(response.text)




# response = model.generate_content(
#           promt)

