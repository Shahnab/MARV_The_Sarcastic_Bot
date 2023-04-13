import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1791/1791365.png", width=150)
st.sidebar.title("Meet MARV: The Sarcastic Bot")
st.sidebar.header("About the Bot:")
st.sidebar.markdown("###### This app is build using GPT3 Open AI model")
st.sidebar.markdown("###### GPT-3 (Generative Pre-trained Transformer 3) is one of the most popular language models")
st.sidebar.markdown("###### GPT-3 is an autoregressive language model that uses deep learning to produce human-like text")
st.sidebar.markdown("###### GPT-3 is trained on over 175 billion parameters on 45 TB of text sourced from all over the internet")

st.sidebar.header("About the GPT-3 Model:")
st.sidebar.markdown(" ###### Davinci is the most capable model in GPT-3 and can do anything that any other model can do, and much more—often with fewer instructions")
st.sidebar.markdown("###### Davinci is able to solve logic problems, determine cause and effect, understand the intent of text, produce creative content, explain character motives, and handle complex summarization tasks")


st.sidebar.header("Powered by")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/1280px-OpenAI_Logo.svg.png", width=150)

st.sidebar.caption("App developed by </Shahnab>")

st.title("Meet MARV: The Sarcastic Bot")
st.caption("Marv is a chatbot that reluctantly answers questions with sarcastic responses")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://ora.sh/-shadows-/marv", width=1100, height=850, scrolling=True)
