import streamlit as st
# from streamlit_option_menu import option_menu
from data_page import data_page
from contact_page import contact_page
from home_page import home_page
from citation_page import citation_page
import hydralit_components as hc

from style import page_style, footer



st.set_page_config(
        # layout='wide',
        page_title='Mesothelioma Spatial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        initial_sidebar_state="collapsed"
        # initial_sidebar_state="collapsed",
)

st.elements.utils._shown_default_value_warning=True


st.markdown(page_style, unsafe_allow_html=True) ## Footer

# change font
with open( "font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# max_width = 2000
# padding_top = 0.5
# padding_right = 0
# padding_left =  0
# padding_bottom = 0
# define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
max_width_str = f"max-width: {95}%;"
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}},
        </style>
        """,
        unsafe_allow_html=True,
    )

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


menu_data = [
        {'icon': "🏠", 'label':"About"},
        {'icon':"📊",'label':"Data"},
        {'icon':"☎️",'label':"Contact"},
        {'icon':"📲",'label':"Citation"},
        
    ]
over_theme = {'txc_inactive': 'white','menu_background':'#0f4d92','txc_active':'black'} #2e5090#0F52BA #048bbc #016490


chosen_tab = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        use_animation= bool(True),
        hide_streamlit_markers=bool(True), 
        sticky_mode='top'
    )


_, cm, _ = st.columns([1,15,1])
with cm: 

    if chosen_tab == "About":
        home_page()
        
    elif chosen_tab == "Contact":
        contact_page()

    elif chosen_tab == "Data":
        data_page()
    
    elif chosen_tab == "Citation":
        citation_page()


    st.divider()
    st.markdown(footer,unsafe_allow_html=True) 
