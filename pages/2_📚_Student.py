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

st.header("About")

st.markdown('''
The Streamlit for Education program enables educators and students to use Streamlit in the classroom and share best practices with the greater community. The first cohort launches in January 2023.

Our Student Ambassador program guides students from building apps to mastering Streamlit.
''')

st.header("Benefits")
st.markdown('''
:ledger: Educational resources

:handshake: A community of educators/learners using Streamlit

:cloud: Hosting support for education-related apps
''')

st.header("Become a Student Ambassador")

st.markdown('''
    <a href="https://bit.ly/streamlit-student-ambassador-app">
        <button type="button" class="btn btn-primary btn-lg px-4 me-sm-3">Apply to become a Student Ambassador!</button>
    </a>
''', unsafe_allow_html=True)
      

load_css()
