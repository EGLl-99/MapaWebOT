from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title= 'Ordenamiento Territorial',page_icon=':tada:',layout='wide')

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
        
        
local_css('style/style.css')

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_88jP8mNam2.json")
img_contact_form= Image.open('Images/Captura de pantalla 2023-03-14 220026.png')


#Header section

with st.container():
    st.subheader('Hi, I am Emilio :wave:')
    st.title('A data analyst from mexico')
    st.write('I am ur daddy bitch')
    st.write('Aqui se puede insertar un link') #st.write('[Accede al link >] (link)')

#---what i do 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )      
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    
    
    
    
    
with st.container():
    st.write('---')
    st.header('My projects')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        st.image(img_contact_form) 
        with text_column:
            st.subheader('Integrar animaciones lottie dentro de la streamlit app')
            st.write(
                """ 
                Aprenda a usar lottie archivos en streamlit
                Animaciones atraen más atencion del publico 
                
                """

            )
            st.markdown("[Learn More >](https://pythonandvba.com)")
            
            
            
with st.container():
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader('How to add a contact form to your streamlit app')
        
        st.write(
            """ 
            Quieres agregar un formularuio de contacto a tu sitio web? 
            En este video te muestro  como implementar un formulario de contacto a tu sitio web 
            
            """

        )
        st.markdown("[Learn More >](https://pythonandvba.com)")
    
    
with st.container():
    st.write('---')
    st.header('Texto para las capas')
    st.write('##')
    
    
    #Documentation Change email address
    contact_form = """ 
    
    <form action="https://formsubmit.co/egonzalezllamas@gmail.com" method="POST">
     <input type= 'hidden' name= '_captcha' value= 'false'>
     <input type="text" name="name" placeholder='Nombre' required>
     <input type="email" name="email" placeholder= 'Correo' required>
     <textarea name= 'message' placeholder= 'Inserta el contexto para tu capa' required></textarea>
     <button type="submit">Enviar</button>
    </form>
    
    """
    
    left_column, right_column= st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_column:
        st.empty()
    