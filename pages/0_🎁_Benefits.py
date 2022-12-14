import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Benefits", page_icon="🎁")

st.header("🎁 Benefits")

st.markdown('''
<table class="table table-striped table-hover">
    <tr>
      <th>Learning materials</td>
      <th>Boilerplate code</td>
      <th>Tools</td>
      <th>Community</td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>
            Access to learning curriculum and presentation slides on getting started with Streamlit
          </li>
          <li>
            Collaborative contribution to learning materials to help shape them to be the best educational material on Streamlit.
          </li>
        </ul>
      </td>
      <td>
        App templates to get you up and running in no time.
      </td>
      <td>
        Additional features/resources for Streamlit Community Cloud.
      </td>
      <td>
        Network with fellow student/educator ambassadors
      </td>
    </tr>
</table>
''', unsafe_allow_html=True)


load_css()
