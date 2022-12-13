import streamlit as st
from utilities import load_css
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
    layout="wide"
)

#st.header("Welcome to Streamlit Education! 👋")
#st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.')

heroes_title = "Level up your data app <br> building skills"
heroes_text = "Streamlit Education is a platform providing students and educators access to tools, learning materials and boilerplate code in order to facilitate the learning and teaching of Streamlit. Whether you’re a novice coder or a veteran, there’s something for everyone. <h3>Register as Educator or Student Ambassador:</h3>"

def heroes(heroes_title_text, heroes_text_text):
    st.markdown(f'''
    <div class="px-4 pt-5 my-5 text-center border-bottom">
        <h1 class="display-4 fw-bold">{heroes_title_text}</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">{heroes_text_text}</p>
          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
            <a href="https://streamlit.io">
                <button type="button" class="btn btn-primary btn-lg px-4 me-sm-3">Educator</button>
            </a>
            <a href="https://streamlit.io">
                <button type="button" class="btn btn-outline-secondary btn-lg px-4">Student</button>
            </a>
          </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

heroes(heroes_title, heroes_text)  
    
# <img src="https://education.streamlit.app/~/+/media/c95e53b82610568716fc642535eb5349ca8b2a22f5608e7087a7360c.png" class="img-fluid border rounded-3 shadow-lg mb-4" alt="Example image" width="700" height="500" loading="lazy">
#image = Image.open('streamlit-cover.png')
#st.write(image)


load_css()


