import streamlit as st
from utils import get_screen_width
from start_page import start_page
from mobile.start_page_mobile import start_page_mobile

st.set_page_config(
        layout='wide',
        page_title='Mesothelioma Spatial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        # initial_sidebar_state="collapsed",
)

max_width_str = f"max-width: {80}%;"
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )
# st.elements.utils._shown_default_value_warning=True

hide_default_format = """
       <style>
       .block-container {
           padding-top: 0rem;
       }
       header[data-testid="stHeader"] {
           display: none;
       }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

width = get_screen_width()

mobile_device = int(width) < 550

if mobile_device :  #  mobile device detected
    start_page_mobile()
else:
    start_page()



