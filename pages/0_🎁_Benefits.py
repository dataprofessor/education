import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Benefits", page_icon="🎁")

st.header("🎁 Benefits")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown('''
    <table class="table table-striped">
        <tr>
          <th>Learning materials</td>
        </tr>
        <tr>
          <td>
            <ul>
              <li>Access to learning curriculum and presentation slides on getting started with Streamlit.</li>
              <li>Collaborative contribution to learning materials to help shape them to be the best educational material on Streamlit.</li>
            </ul>
          </td>
        </tr>
    </table>
    ''', unsafe_allow_html=True)
    
with col2:
    st.markdown('''
        <table class="table table-striped">
            <tr>
              <th>Boilerplate code</td>
            </tr>
            <tr>
              <td>
                <ul>
                  <li>App templates to get you up and running in no time.</li>
                  <li>Curation of example apps from various domains that can help inspire your own app creations.</li>
                </ul>
              </td>
            </tr>
        </table>
        ''', unsafe_allow_html=True)
    
with col3:
    st.markdown('''
    <table class="table table-striped">
        <tr>
          <th>Tools</td>
        </tr>
        <tr>
          <td>
            <ul>
              <li>Additional features/resources for Streamlit Community Cloud.</li>
              <li>Exclusive pre-release access to new features in Streamlit and Streamlit Community Cloud.</li>
            </ul>
          </td>
        </tr>
    </table>
    ''', unsafe_allow_html=True)
    
with col4:
    st.markdown('''
    <table class="table table-striped">
        <tr>
          <th>Community</td>
        </tr>
        <tr>
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
