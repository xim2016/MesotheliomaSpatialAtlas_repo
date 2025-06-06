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


width = get_screen_width()

mobile_device = int(width) < 550

if mobile_device :  #  mobile device detected
    start_page_mobile()
else:
    start_page()



