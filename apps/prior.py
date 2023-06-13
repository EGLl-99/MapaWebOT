import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Initialize()
#st.set_page_config(layout='wide')


def app():
    st.title('Capas Priorizadas')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    markdown= """
        
        En este sitio se muestra el resultado de realizar una evaluación multicriterio considerando 
        factores propios del ordenamiento territorial de Yucatan
        
    """
    
    
    capa1= ee.Image('users/emiliogonzalez/Priorizacion1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#41DE07','#FFA533','#FF3333'], 'min':1,'max':4}
    
    Map.addLayer(capa1,vis1,'Transporte')
    
    Map.to_streamlit(height=750)