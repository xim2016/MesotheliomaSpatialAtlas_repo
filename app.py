import streamlit as st
from utils import get_screen_width
from start_page import start_page
from mobile.start_page_mobile import start_page_mobile

# For Google analytics track
import streamlit.components.v1 as components

def inject_google_tag():
    GA_JS = """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-GJ8KNPB8W8"></script>
    <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
        
          gtag('config', 'G-GJ8KNPB8W8');
    </script>
    """
    st.write("")
    components.html(GA_JS, height=0, width=0)

# Call the function at the start of your app
inject_google_tag()
# end of the track

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



