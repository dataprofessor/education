import streamlit as st
from utilities import load_css
from streamlit_image_select import image_select

st.set_page_config(page_title="Educator", page_icon="🍎", initial_sidebar_state="expanded", layout="wide")

# Initialization
if 'img' not in st.session_state:
    st.session_state['img'] = "img/educator_1.png"

st.header("🍎 Educator")

placeholder = st.empty()
st.session_state['img'] = image_select("Double click on an image below:", ["img/educator_1.png", "img/educator_2.png", "img/educator_3.png", "img/educator_4.png", "img/educator_5.png"])
placeholder.image(st.session_state['img'])

st.header("About")

st.markdown('''
The Streamlit for Education program enables educators and students to use Streamlit in the classroom and share best practices with the greater community. The first cohort launches in January 2023.

Our Educator Ambassador program supports educators using Streamlit in the classroom.
''')

st.header("Benefits")
st.markdown('''
:ledger: Educational resources

:handshake: A community of educators/learners using Streamlit

:cloud: Hosting support for education-related apps
''')

st.header("Apply")

st.markdown('''
    <a href="https://bit.ly/streamlit-educators">
        <button type="button" class="btn btn-primary btn-lg px-4 me-sm-3">Apply to become an Educator Ambassador!</button>
    </a>
''', unsafe_allow_html=True)
            
load_css()
