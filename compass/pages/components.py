import dash_leaflet as dl
import dash_mantine_components as dmc
from dash import html

map_component = dl.Map(children=[], center=[45.5019, -73.5674], zoom=11, style={'height': '50vh'}, id="map-component")

button = dmc.Button(children="Get Data", id="get_data")