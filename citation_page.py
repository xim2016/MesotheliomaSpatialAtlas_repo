# from style import define_layout
# import streamlit as st
# # from descriptions import Desc

# def citation_page():
    
#     max_width = '90%'
#     padding_top = '0rem'
#     padding_right = '0rem'
#     padding_left = '13rem'
#     padding_bottom = '0rem'
#     define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   
    
#     # st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
#     st.markdown("**Citation guidelines for the Mesothelioma Spatial Atlas**")
#     st.markdown("While we encourage you to use these resources for your research and commercial purposes, we want to ensure that our content is given proper citation in all cases where it is used.") 
    
#     st.markdown("###")
#     # st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
#     # st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_general}</h4>", unsafe_allow_html=True) 
#     st.markdown("**General citation for the Mesothelioma Spatial Atlas**") 
#     st.markdown("If you cite or display any content, or reference this website, in any format, written or otherwise, including print or web publications, presentations, grant applications, websites, other online applications such as blogs, or other works, you must include a reference to our website: https://mesotheliomaspatialatlas.streamlit.app.")

#     st.markdown("###")
#     # st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
#     st.markdown("**Specific citation for image, chanel or data**")
#     st.markdown("If you use images, or reference a specific image type, or other data downloaded from the site, in addition to citing the Mesothelioma Spatial Atlas, please also cite the specific image,  or data used and the URL that links directly to that information in a manner that will allow a third party to navigate to that image or data on the site.") 
    
#     st.markdown("###")
#     # st.markdown(f"<p style='color: black; font-weight: bold'>Citation</h3>", unsafe_allow_html=True)
#     st.markdown("**Citation**")
#     st.markdown("If you find the images or data from this website helpful, please cite the paper: https://www.biorxiv.org/content/10.1101/2023.09.06.556559v1")

#     st.markdown("#")

from style import define_layout
import streamlit as st
import urllib.parse
# from descriptions import Desc

def citation_page():
    
    # max_width = '90%'
    # padding_top = '0rem'
    # padding_right = '0rem'
    # padding_left = '13rem'
    # padding_bottom = '0rem'
    # define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   
    
    # st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
    st.markdown('<span style="font-size:25px;"> **Citation guidelines for the Mesothelioma Spatial Atlas**</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:18px;">While we encourage you to use these resources for your research and commercial purposes, we want to ensure that our content is given proper citation in all cases where it is used.</span>', unsafe_allow_html=True) 
    
    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
    # st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_general}</h4>", unsafe_allow_html=True) 
    st.markdown('<span style="font-size:21px;"> **General citation for the Mesothelioma Spatial Atlas**</span>', unsafe_allow_html=True) 
    st.markdown('<span style="font-size:18px;">If you cite, display, or reference this website in any format—print, web, presentations, grant applications, blogs, or other works—you must include the reference: https://mesotheliomaspatialatlas.streamlit.app.</span>', unsafe_allow_html=True)

    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
    st.markdown('<span style="font-size:21px;">**Specific citation for image, chanel or data**</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:18px;">If you use images, or reference a specific image type, or other data downloaded from the site, in addition to citing the Mesothelioma Spatial Atlas, please also cite the specific image,  or data used and the URL that links directly to that information in a manner that will allow a third party to navigate to that image or data on the site.</span>', unsafe_allow_html=True) 
    
    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>Citation</h3>", unsafe_allow_html=True)
    st.markdown('<span style="font-size:21px;">**Citation**</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size:18px;">If you find the images or data from this website helpful, please cite the paper: https://aacrjournals.org/cancerrescommun/article/4/8/2133/747011/Spatial-Landscape-of-Malignant-Pleural-and</span>', unsafe_allow_html=True)

   

    
    st.markdown('<span style="font-size:18px;">Click below for a downloable citation</span>', unsafe_allow_html=True)
    

    #citation in APA format and MLA format
    apa_citation= "Ma, X., Lembersky, D., Kim, E. S., Becich, M. J., Testa, J. R., Bruno, T. C., & Osmanbeyoglu, H. U. (2024). Spatial Landscape of Malignant Pleural and Peritoneal Mesothelioma Tumor Immune Microenvironments. Cancer research communications, 4(8), 2133–2146. https://doi.org/10.1158/2767-9764.CRC-23-0524"
    mla_citation="Ma, Xiaojun et al. “Spatial Landscape of Malignant Pleural and Peritoneal Mesothelioma Tumor Immune Microenvironments.” Cancer research communications vol. 4,8 (2024): 2133-2146. doi:10.1158/2767-9764.CRC-23-0524"
 

    c1,c2,c3=st.columns([0.3,1,2.5])

    with c1:
        
     #third set of button for APA format
        citationapa_data=apa_citation
        encodedapa_data=urllib.parse.quote(citationapa_data)    
        apa_button =  f"""
        <style>
            .button {{
                display: inline-block;
                padding: 10px 15px;
                font-size: 16px;
                font-weight: bold;
                color: white !important;
                background-color: #003594; /* Pitt Royal Blue */
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.2s
            }}
            .button:hover {{
                background-color: #00205B; /* Medium Blue on hover */
                transform: scale(1.05); /* Slight zoom effect */
            }}
            .button:active {{
                background-color: #003594; /* Pitt Royal Blue on click */
                transform: scale(0.95); /* Slight shrink effect */
            }}
        </style>    
        <a href="data:text/plain;charset=utf-8,{encodedapa_data}" download="citations_apa.txt" class="button
        ">
            APA
        </a>
        """
        st.markdown(apa_button,  unsafe_allow_html=True)
   

    with c2:

        citationmla_data=mla_citation
        encodedmla_data=urllib.parse.quote(citationmla_data)    
        mla_button =  f"""
        <style>
            .button {{
                display: inline-block;
                padding: 10px 15px;
                font-size: 16px;
                font-weight: bold;
                color: white !important;
                background-color: #003594; /* Pitt Royal Blue */
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.2s
            }}
            .button:hover {{
                background-color: #00205B; /* Medium Blue on hover */
                transform: scale(1.05); /* Slight zoom effect */
            }}
            .button:active {{
                background-color: #003594; /* Pitt Royal Blue on click */
                transform: scale(0.95); /* Slight shrink effect */
            }}
        </style>    
        <a href="data:text/plain;charset=utf-8,{encodedmla_data}" download="citations_mla.txt" class="button
        ">
            MLA
        </a>
        
        """
        st.markdown(mla_button,  unsafe_allow_html=True)
    with c3: 
        # img =  Image.open('./assets/figures/Lung_Line.jpg')
        # st.image(img)  
        st.image("./assets/figures/Lung_Line.jpg", width=300)

    st.markdown("#")

    import sys
    st.write(f"Running Python version: `{sys.version}`")
