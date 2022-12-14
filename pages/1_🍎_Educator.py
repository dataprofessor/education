import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Educator", page_icon="🍎")

st.header("🍎 Educator")

st.markdown('''
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
''', unsafe_allow_html=True)

st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.

Fusce ultrices tincidunt elit imperdiet dapibus. Nunc condimentum fermentum lacinia. Duis vestibulum neque posuere lorem tempus iaculis. Nulla ultrices accumsan est quis ullamcorper. Morbi convallis congue dui eu congue. Quisque laoreet turpis commodo luctus varius. Aliquam et iaculis erat. Mauris bibendum sem leo, id ultricies sapien viverra sed. Nunc id erat quis justo sagittis viverra ut id erat.

Duis ultricies, sem eu fermentum fermentum, nisl tellus egestas odio, at placerat augue quam eget justo. Nullam facilisis porttitor ante, vitae blandit odio dapibus at. Nam tellus arcu, tristique sit amet posuere ut, posuere id nibh. Fusce ut diam dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc metus sapien, feugiat sed diam in, facilisis sollicitudin eros. Quisque quis ex et nunc pellentesque vestibulum. Praesent interdum molestie orci, id faucibus lorem blandit consequat. Vivamus aliquam, erat eu facilisis lacinia, felis nunc tristique lectus, iaculis pretium lectus massa eget risus. Pellentesque rhoncus arcu vel elementum venenatis. Ut in blandit libero, eget facilisis magna. Morbi aliquam elit ut neque imperdiet scelerisque.
''')

load_css()
