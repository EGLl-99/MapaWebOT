import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Initialize()
#st.set_page_config(layout='wide')
#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
        
        
local_css('style/style.css')


def app():
    st.title('Transporte')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')

def app():
    st.title('Clima')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    markdown= """
        
        El clima en Yucatán es cálido y subhúmedo en la mayor parte del estado, con lluvias en verano. La temperatura media anual es de 26°C, y la temperatura máxima promedio es alrededor de 36°C y se presenta en el mes de mayo, mientras que la temperatura mínima promedio es de 18°C y se presenta en enero. La humedad es alta y las temperaturas son elevadas y constantes. La mejor época para viajar es en enero, mientras que se debe evitar la temporada de lluvias de junio a octubre
        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Clima1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

# legend_dict = {
#     'Idoneo': '#008000',
#     'Optimo': '#41DE07',
#     'Medianamente optimo ': '#FFFF00',
#     'Ligeramente factible': '#FFA533',
#     'No es factible': '#FF3333'
# }


vis1= {
    'palette':['#008000','#41DE07','#FFFF00','#FFA533','#FF3333'],
    'min':1,
    'max':5
}



    #vis1= {'palette':['#008000','#41DE07','#FFFF00','#FFA533','#FF3333'], 'min':1,'max':5}
# Map.add_legend(legend_dict=legend_dict)   
Map.addLayer(capa1,vis1,'Clima')
Map.to_streamlit(height=750)

    
    
    
