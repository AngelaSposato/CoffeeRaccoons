from dash import Dash
import dash_leaflet as dl
# 45.5019° N, 73.5674° W
app = Dash(__name__, title='Montreal Compass')
app.layout = dl.Map(dl.TileLayer(), center=[45.5019, -73.5674], zoom=6, style={'height': '50vh'})

if __name__ == '__main__':
    app.run_server(debug=True)