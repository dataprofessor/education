import streamlit as st
from utilities import load_css
from streamlit_image_select import image_select

st.set_page_config(page_title="Student", page_icon="📚", initial_sidebar_state="expanded", layout="wide")

# Initialization
if 'img' not in st.session_state:
    st.session_state['img'] = "img/student_1.png"
    
st.header("📚 Student")

st.image(st.session_state['img'])
st.session_state['img'] = image_select("Double click on an image below:", ["img/student_1.png", "img/student_2.png", "img/student_3.png", "img/student_4.png", "img/student_5.png"])


load_css()
