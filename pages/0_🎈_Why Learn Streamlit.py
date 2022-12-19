import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Why Learn Streamlit?", page_icon="🎈", initial_sidebar_state="expanded")

st.header("🎈 Why Learn Streamlit?")

st.markdown('''
#### 🐍 Importance of Python
Python has emerged as one of the most popular programming languages to learn owing to its simplicity, wide utility and demand in the job market. According to the [Python Developers Survey 2021](https://lp.jetbrains.com/python-developers-survey-2021/), the top use cases for Python includes data analysis, web development and machine learning, which are areas well served by the Streamlit library. 

#### 🕹️ Streamlit as a UI layer of Python
Streamlit is known by the community as a tool that can confer a UI front-end to any Python script while requiring minimal coding. A typical user can go from idea to an app prototype in a few minutes/hours.

#### 🤝 Fosters collaboration
As the future of work and education is heavily reliant on remote work and collaboration, Streamlit technology enables user to quickly prototype a fully functional data-driven app that comes equipped with both interactive input and output widgets. The ability to share ideas as apps foster the materialization of ideas and collaboration, which are instrumental to move projects forward.

#### 🤔 Receiving feedbacks
As such, apps are great ways for receiving additional comments and feedbacks from a wide range of stakeholders (both technical and non-technical) that could help reiterate the app improvement process. An additional benefit of apps is that they allow users to readily interact with the app without the need to setup hardware/software.

#### 💼 Job-readiness
Becoming proficient in Streamlit help prepare students to use the same technology that are already used in the industry.
''')

load_css()
