import streamlit as st
from PIL import Image
from descriptions import Desc
from style import define_layout

@st.cache_data
def load_homeImg():
    img =  Image.open('./assets/figures/home.png')
    st.image(img)  

def home_page():

    # max_width = '90%'  # '1900px'
    # padding_top = '0rem'
    # padding_right = '0rem'
    # padding_left = '13rem'
    # padding_bottom = '0rem'
    # define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
   
    _,m1,_ = st.columns([1,5,1])

    
    with m1:  
        load_homeImg()
        

    #     # st.markdown('---')
    # with m2_:
        st.markdown("#")
        st.markdown(f"<p style='text-align: justify; color: black; font-size: 14px'>{Desc.Abstract}</h4>", unsafe_allow_html=True) 
        st.markdown("#")
        st.markdown(' Read our paper from here 👉 https://aacrjournals.org/cancerrescommun/article/4/8/2133/747011/Spatial-Landscape-of-Malignant-Pleural-and')    

       
    
