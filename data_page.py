import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image
from utils import get_orderedList, get_imageNames, load_HEImages, load_coreImages, show_plotly_image, get_core_feature, get_coreStatistic
from style import define_layout
import os
import requests

def disable_other_checkboxes(*other_checkboxes_keys):
    # if current one is trun to false, reset it to true
    if st.session_state[other_checkboxes_keys[-1]] == False:
        st.session_state[other_checkboxes_keys[-1]] = True
        
    for checkbox_key in other_checkboxes_keys[:-1]:
        st.session_state[checkbox_key] = False
        
def get_current_checkedBox(options):
    key = list(options.keys())[list(options.values()).index(True)]
    return (key)      


# max_width_str = f"max-width: {95}%;"
# st.markdown(f"""
#         <style>
#         .appview-container .main .block-container{{{max_width_str}}}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


def data_page():
    
    
    REPO_HE = 'https://raw.githubusercontent.com/xim2016/MesotheliomaSpatialAtlas_data/main/H%26E_level1'
    REPO_TMA = 'https://raw.githubusercontent.com/xim2016/MesotheliomaSpatialAtlas_data/main'
 

    # max_width = '100%'
    # padding_top = '0rem'
    # padding_right = '0rem'
    # padding_left = '0rem'
    # padding_bottom = '0rem'
    # define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    PATH_IMG_TMA = "./data/core_image"
    PATH_IMG_HE = "./data/core_image/H&E_level1"  
    path_img_logo = "./data/core_image/H&E_logo" 

    c1_IDs = ["Institute", "Classification","CaseType","subtype", "Grade"]
    c1_names = ["Institute", "Classification","Case type","Subtype", "Tumor grade"]
    c1 = st.columns([3,3,3,3,3])
    cs1 = dict()
    for i in range(5):
        cs1[i] = c1[i].selectbox(
                    c1_names[i],
                    get_orderedList(c1_IDs[i]),
                    key = c1_IDs[i]
                )
    

    c2_IDs = ["Gender", "DiagnosisAge","AsbestosExposure","Race", "smoking"]
    c2_names = ["Gender", "Diagnosis age","Asbestos exposure","Race", "Smoking"]
    c2 = st.columns([3,3,3,3,3])
    cs2 = dict()
    for i in range(5):
        cs2[i] = c2[i].selectbox(
                    c2_names[i],
                    get_orderedList(c2_IDs[i]),
                    key = c2_IDs[i]
                )
        
    with st.sidebar:
        

        #H&E use image_names , others use core_ids as image names

        image_names, core_ids, core_ids2 = get_imageNames(cs1, cs2, c1_IDs,c2_IDs)
        images, showedImage_names, showedCore_ids, showedCore_ids2 = load_HEImages(path_img_logo , list(image_names), list(core_ids), list(core_ids2))

        if len(images) > 0 :
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown("### Please select a core.", True)
            st.write("")

            # st.markdown(f"##### ( {len(images)} cores )", True)
            
            clicked = clickable_images(
                images, 
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                img_style={"margin": "10px", "height": "70px"},
            )
        else:
            st.write("No core for current selection.")


    
    if len(images) == 0:
        for i in range(20):
            st.markdown("#")
            
    if len(images) > 0 :

        st.divider()

        if clicked == -1: clicked = 0

        vargs0 = ["H&E"]
        vargs1 = ["mIF", "CD4", "CD8", "CD20", "CD68", "FOXP3", "panCK"]
        vargs2 = ["mIF ", "CD56", "CD11c", "BAP1","NF2", "MTAP","LAG3"] 
        vargs = vargs0 +  vargs1 + vargs2   

        chanel_images = load_coreImages(showedImage_names[clicked],showedCore_ids[clicked],showedCore_ids2[clicked] )
        ls_images = list(chanel_images.values())

        clab = st.columns([1,7,7])
        
        clab[1].markdown( '<p style="font-size: 14px;  font-weight: bold"> Panel-Marker </p>',  unsafe_allow_html=True) 
        clab[2].markdown(' <p style="font-size: 14px;  font-weight: bold"> Panel-Protein </p>',  unsafe_allow_html=True)

        cimg = st.columns(15)

        for i in range(15):
            with cimg[i]:
                st.markdown(ls_images[i], unsafe_allow_html=True)
                st.markdown( f"<p style='font-size: 14px;  font-weight: normal; text-align: center'>{vargs[i]}</p>",  unsafe_allow_html=True) 

        st.divider()
        c1, c2,_,c3 = st.columns([1.5, 7,0.5,2.5])

        with c1:
            # st.markdown("#### Image type")
            st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Image type</p>',  unsafe_allow_html=True) #sans-serif   Soin Sans Pro
    
            option2dir = {"H&E": f"{REPO_HE}",
                        "mIF": f"{REPO_TMA}/panel1/multi",
                        "CD4": f"{REPO_TMA}/panel1/CD4",
                        "CD8": f"{REPO_TMA}/panel1/CD8",
                        "CD20": f"{REPO_TMA}/panel1/CD20",
                        "CD68": f"{REPO_TMA}/panel1/CD68",
                        "FOXP3": f"{REPO_TMA}/panel1/FOXP3",
                        "panCK": f"{REPO_TMA}/panel1/panCK",
                        "mIF ": f"{REPO_TMA}/panel2/multi2",
                        "CD56": f"{REPO_TMA}/panel2/CD56",
                        "CD11c": f"{REPO_TMA}/panel2/CD11c",
                        "BAP1": f"{REPO_TMA}/panel2/BAP1",
                        "NF2": f"{REPO_TMA}/panel2/NF2",
                        "MTAP": f"{REPO_TMA}/panel2/MTAP",
                        "LAG3": f"{REPO_TMA}/panel2/LAG3"
            }


            options = dict()
            for key in vargs0:
                options[key] = st.checkbox(
                key,
                value=True,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )
            # st.markdown("###### Panel-marker")
            for key in vargs1:
                options[key] = st.checkbox(
                key,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )
            # st.markdown("###### Panel-protein")
            for key in vargs2:
                options[key] = st.checkbox(
                key,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )

            
            # rd = st.radio("", ("H&E","", "mIF", "mIF ", "CD4", "CD8", "CD56", "CD68", "CD11c", "FOXP3","CD20", "BAP1","NF2", "MTAP","LAG3" ))

        with c2:
        

            option = get_current_checkedBox(options)

            dir = option2dir[option]
        
            if option == "H&E":
                filename = f"{showedImage_names[clicked]}.jpg"
            elif option in vargs1 :   
                filename = f"{showedCore_ids[clicked]}_composite_image.jpg"
            else:
                filename = f"{showedCore_ids2[clicked]}_composite_image.jpg"

            imgurl = f"{dir}/{filename}"
            imgurl = imgurl.replace(" ", "%20") # replace space
            imgurl = imgurl.replace("#", "%23") # replace # 

            def exists(path): #not used
                r = requests.head(path)
                return r.status_code == requests.codes.ok
            
            def is_url_image(image_url):
                image_formats = ("image/png", "image/jpeg")
                r = requests.head(image_url)
                # st.write(r.headers["content-type"])
                if r.headers["content-type"] in image_formats:
                    return True
                return False

            if is_url_image(imgurl):
                #show_plotly_image(imgurl, 750)
                st.image(imgurl)
				
                img = requests.get(imgurl)
                image_data = img.content
				
                st.markdown(f"[Click here to view full size image. :material/open_in_new:]({imgurl})")
				
				# Button to open image in another window
				
                st.download_button(
                      label="Download image",
                      data=image_data,
                      file_name=filename,
                      mime="image/png",
                      type="primary",
                      icon=":material/download:"
				)
            else:
                st.markdown("#")
                info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Image datas is not available for this core.</p>'  #sans-serif   Soin Sans Pro
                st.markdown(info, unsafe_allow_html=True)


        
            # st.image(imgfile)

        with c3:
            
            # st.markdown("#### Core feature", True)
            st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Core feature</p>',  unsafe_allow_html=True) 
            st.write("")
            st.write("")    


            core_id = showedCore_ids[clicked]

            fetu1, fetu2, fetu_plus = get_core_feature(c1_IDs, c2_IDs, core_id)
            for i in range(5):
                st.markdown(f"**{c1_names[i]}** : {fetu1[i]}", True)
            for i in range(5):
                st.markdown(f"**{c2_names[i]}** : {fetu2[i]}", True)
                # st.markdown(f"**:black[{c2_names[i]}]** : {fetu2[i]}", True) 
            for item in fetu_plus.keys():
                st.markdown(f"**{item}** : {fetu_plus[item]}", True)   

            percent, count1, count2 = get_coreStatistic(core_id, option)
            if option in vargs1:
                count = count1
            else:
                count = count2
            st.markdown(f"**Number of cells** : {count}", True) 
            # st.markdown(f"**{option} percentage** : {percent}", True)  

            if option != "H&E":
                st.divider()
                st.markdown("**DAPI in :blue[blue color]**")


    
