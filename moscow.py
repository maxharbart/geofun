import folium
import json


map = folium.Map(location=[55.753220, 37.622513], zoom_start=10)

def color(name):
    if name == 'Центральный':
        return 'red'
    else:
        return 'green'


folium.GeoJson(open('ao.geojson', 'r', encoding='utf-8-sig').read(),
               name='boros',
               style_function = lambda x: {'fillColor': color(x['properties']['NAME'])},
               tooltip = folium.GeoJsonTooltip(fields=('NAME',), aliases=('Район: ',), show=True)
               ).add_to(map)



style1 = {'fillColor': 'red'}
style2 = {'fillColor': 'orange'}
style3 = {'fillColor': 'yellow'}


map.save('moscow.html')