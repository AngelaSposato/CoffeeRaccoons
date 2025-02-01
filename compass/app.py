from dash import Dash
import dash_mantine_components as dmc
import dash_leaflet as dl
from dash_extensions.javascript import assign
from dash import (
    Dash,
    html,
    dcc,
    page_registry,
    Output,
    Input,
)
from pages.components import button, map_component
from functions import get_db_data, get_geo_data, get_db, get_pin_icon


app = Dash(
    __name__,
    title="Montreal Compass",
)

links = [html.Div(dcc.Link(p["name"], href=p["path"])) for p in page_registry.values()]

app.layout = dmc.MantineProvider(
    children=[
        html.Div(links),
        button,
        # db_table,
        map_component,  
    ]
)


@app.callback(
    Output("map-component", component_property="children"),
    Input("get_data", component_property="n_clicks"),
)
def populate_map(clicks):
    db = get_db("MontrealCompass")
    data = get_db_data(db, "listing_data")
    geojson = get_geo_data(data)
    # draw_flag = assign(
    #     """function(feature, latlng){
    #     const flag = L.icon({iconUrl: `./assets/map-pin.png`, iconSize: [64, 64]});
    #     return L.marker(latlng, {icon: flag});
    #     }"""
    # )
    return [dl.TileLayer(), dl.GeoJSON(data=geojson, cluster=True, zoomToBoundsOnClick=True, )]


if __name__ == "__main__":
    app.run_server(debug=True)
