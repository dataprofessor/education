import streamlit as st

def load_css():
    with open("bootstrap.min.css") as g:
        st.markdown('<style>{}</style>'.format(g.read()), unsafe_allow_html=True)
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
