import streamlit as st
from utilities import load_css
from PIL import Image

st.set_page_config(
    page_title="Welcome to Streamlit Education",
    page_icon="🏠",
    layout="wide"
)

heroes_title = 'Level up your data app <br> building skills'
heroes_text = '''
Streamlit Education is a platform providing students and educators access to tools, learning materials and boilerplate code in order to facilitate the learning and teaching of Streamlit. Whether you’re a novice coder or a veteran, there’s something for everyone. 
<br><br>
✍️ Register as an Educator or a Student Ambassador:
'''

st.markdown(heroes_title, unsafe_allow_html=True)
st.markdown(heroes_text, unsafe_allow_html=True)

educator = st.button('Educator')
if educator:
    st.markdown('<meta http-equiv="refresh" content="0;url=https://bit.ly/streamlit-educators">', unsafe_allow_html=True)

load_css()


