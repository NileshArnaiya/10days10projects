
# coding: utf-8

# In[9]:


import cv2
import folium
import pandas as pd

map = folium.Map(location=(38.8026,-117.224121),zoom_start=6, attr="<a href=https://buildawn.com></a>")
data = pd.read_csv('Volcanoes.txt')
latitude = list(data['LAT'])
longitude = list(data['LON'])
pop = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'blue'


for lat,lng,pop in zip(latitude,longitude,pop):
    map.add_child(folium.CircleMarker(location=[lat,lng], popup = pop, radius= 6, 
                                      fill_color= color_producer(pop), color='grey', fill_opacity=0.7))

    
map.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save("Woahmymap.html")


