import streamlit as st
from utilities import load_css
from streamlit_image_select import image_select

st.set_page_config(page_title="Educator", page_icon="🍎", initial_sidebar_state="expanded", layout="wide")

# Initialization
if 'img' not in st.session_state:
    st.session_state['img'] = "img/educator_1.png"

st.header("🍎 Educator")


st.image(st.session_state['img'])
st.session_state['img'] = image_select("Label", ["img/educator_1.png", "img/educator_2.png", "img/educator_3.png", "img/educator_4.png", "img/educator_5.png"])


st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.

Fusce ultrices tincidunt elit imperdiet dapibus. Nunc condimentum fermentum lacinia. Duis vestibulum neque posuere lorem tempus iaculis. Nulla ultrices accumsan est quis ullamcorper. Morbi convallis congue dui eu congue. Quisque laoreet turpis commodo luctus varius. Aliquam et iaculis erat. Mauris bibendum sem leo, id ultricies sapien viverra sed. Nunc id erat quis justo sagittis viverra ut id erat.

Duis ultricies, sem eu fermentum fermentum, nisl tellus egestas odio, at placerat augue quam eget justo. Nullam facilisis porttitor ante, vitae blandit odio dapibus at. Nam tellus arcu, tristique sit amet posuere ut, posuere id nibh. Fusce ut diam dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc metus sapien, feugiat sed diam in, facilisis sollicitudin eros. Quisque quis ex et nunc pellentesque vestibulum. Praesent interdum molestie orci, id faucibus lorem blandit consequat. Vivamus aliquam, erat eu facilisis lacinia, felis nunc tristique lectus, iaculis pretium lectus massa eget risus. Pellentesque rhoncus arcu vel elementum venenatis. Ut in blandit libero, eget facilisis magna. Morbi aliquam elit ut neque imperdiet scelerisque.
''')

load_css()
