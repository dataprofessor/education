import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Benefits", page_icon="🎁")

st.header("🎁 Benefits")

st.markdown('''
<table class="table table-striped">
    <tr>
      <th>Learning materials</td>
      <th>Boilerplate code</td>
      <th>Tools</td>
      <th>Community</td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>Access to learning curriculum and presentation slides on getting started with Streamlit.</li>
          <li>Collaborative contribution to learning materials to help shape them to be the best educational material on Streamlit.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>App templates to get you up and running in no time.</li>
          <li>Curation of example apps from various domains that can help inspire your own app creations.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Additional features/resources for Streamlit Community Cloud.</li>
          <li>Exclusive pre-release access to new features in Streamlit and Streamlit Community Cloud.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Network with fellow student/educator ambassadors.</li>
          <li>Share best practices.</li>
        </ul>
      </td>
    </tr>
</table>
''', unsafe_allow_html=True)


load_css()
