import streamlit as st
from utilities import load_css
from streamlit_image_select import image_select

st.set_page_config(page_title="Educator", page_icon="🍎", initial_sidebar_state="expanded", layout="wide")

# Initialization
if 'img' not in st.session_state:
    st.session_state['img'] = "img/educator_1.png"

st.header("🍎 Educator")


st.image(st.session_state['img'])
st.session_state['img'] = image_select("Double click on an image below:", ["img/educator_1.png", "img/educator_2.png", "img/educator_3.png", "img/educator_4.png", "img/educator_5.png"])

st.header("Become an Educator Ambassador")

st.markdown('''
    <a href="https://bit.ly/streamlit-educators">
        <button type="button" class="btn btn-primary btn-lg px-4 me-sm-3">Sign up!</button>
    </a>
''', unsafe_allow_html=True)
            
load_css()
