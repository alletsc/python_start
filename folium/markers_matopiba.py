import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import folium
from folium.plugins import MarkerCluster
import json


expo = pd.read_csv('expo2.csv')
df = expo
df1 = df.drop(['Unnamed: 0'], axis=1)

m_expo = folium.Map(location=[-6.8074226, -47.6999202],  zoom_start=6,
                    tiles='Stamen Terrain')

for index, linha in df1.iterrows():
    folium.Marker([linha['LAT'], linha['LONG']],
                  popup=linha['EXPORTAÇÃO U$'],
                  tooltip=linha['MUNICIPIO'],
                  icon=folium.Icon(color='darkgreen', icon_color='#45B39D',  # cores personalizaveis com html
                                   icon='leaf',  # icon font awesome ou bootstrap glyphicons
                                   prefix='fa')
                  ).add_to(m_expo)


suape = folium.CircleMarker(location=[-8.3944,  -34.9741],
                            popup='Porto de Suape',
                            tooltip='Porto de Suape',
                            icon=folium.Icon(color='red')
                            ).add_to(m_expo)

itaqui = folium.CircleMarker(location=[-2.5776,  -44.3673],
                             popup='Porto de Itaqui',
                             tooltip='Porto de Itaqui',
                             icon=folium.Icon(color='red')
                             ).add_to(m_expo)

pecem = folium.CircleMarker(location=[-3.5495,  -38.8108],
                            popup='Porto de Pécem',
                            tooltip='Porto de Pécem',
                            icon=folium.Icon(color='red')
                            ).add_to(m_expo)

folium.TileLayer('openstreetmap').add_to(m_expo)
folium.TileLayer('stamentoner').add_to(m_expo)
folium.TileLayer('stamenterrain').add_to(m_expo)

folium.TileLayer('cartodbpositron').add_to(m_expo)

folium.LayerControl().add_to(m_expo)

m_expo.save('mapa.html')
