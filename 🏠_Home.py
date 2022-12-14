import streamlit as st
from utilities import load_css
from PIL import Image

st.set_page_config(
    page_title="Welcome to Streamlit Education",
    page_icon="🏠",
    layout="wide"
)

heroes_title = "Level up your data app <br> building skills"
heroes_text = """Streamlit Education is a platform providing students and educators access to tools, learning materials and boilerplate code in order to facilitate the learning and teaching of Streamlit. Whether you’re a novice coder or a veteran, there’s something for everyone. 
<br><br>
✍️ Register as an Educator or a Student Ambassador:
"""

def heroes(heroes_title_text, heroes_text_text):
    st.markdown(f'''
    <div class="px-4 pt-5 my-5 text-center border-bottom">
        <h1 class="display-4 fw-bold">{heroes_title_text}</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4"><b>{heroes_text_text}</b></p>
          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
            <a href="https://bit.ly/streamlit-educators">
                <button type="button" class="btn btn-primary btn-lg px-4 me-sm-3">Educator</button>
            </a>
            <a href="https://bit.ly/streamlit-student-ambassador-app">
                <button type="button" class="btn btn-outline-secondary btn-lg px-4">Student</button>
            </a>
          </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

heroes(heroes_title, heroes_text)  



load_css()

