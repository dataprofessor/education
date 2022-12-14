import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Educator", page_icon="🍎")

st.header("🍎 Educator")

st.markdown('''
  <style>
    <link href="carousel.css" rel="stylesheet">
  </style>
''', unsafe_allow_html=True)

st.markdown('''
  <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

        <div class="container">
          <div class="carousel-caption text-start">
            <h1>Example headline.</h1>
            <p>Some representative placeholder content for the first slide of the carousel.</p>
            <p><a class="btn btn-lg btn-primary" href="#">Sign up today</a></p>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

        <div class="container">
          <div class="carousel-caption">
            <h1>Another example headline.</h1>
            <p>Some representative placeholder content for the second slide of the carousel.</p>
            <p><a class="btn btn-lg btn-primary" href="#">Learn more</a></p>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#777"/></svg>

        <div class="container">
          <div class="carousel-caption text-end">
            <h1>One more for good measure.</h1>
            <p>Some representative placeholder content for the third slide of this carousel.</p>
            <p><a class="btn btn-lg btn-primary" href="#">Browse gallery</a></p>
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
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
