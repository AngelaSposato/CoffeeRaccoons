import dash_mantine_components as dmc
import dash_leaflet as dl
from dash import Dash, html, dcc, page_registry, Output, Input, State, _dash_renderer, callback_context
from pages.components import layout
from functions import get_db_data, get_geo_data, get_db, create_listing, get_one_listing 

_dash_renderer._set_react_version("18.2.0")

db = get_db("MontrealCompass")

app = Dash(
    __name__,
    title="Montreal Compass",
    prevent_initial_callbacks=True,
)

links = [html.Div(dcc.Link(p["name"], href=p["path"])) for p in page_registry.values()]

app.layout = layout


# @app.callback(
#     Output("map-component", component_property="children"),
#     allow_duplicate=True,
# )
# def populate_map(clicks):
#     db = get_db("MontrealCompass")
#     data = get_db_data(db, "listing_data")
#     geojson = get_geo_data(data)
#     return [dl.TileLayer(), dl.GeoJSON(data=geojson, cluster=True, zoomToBoundsOnClick=True, )]

# @app.callback(
#     Output("mantine-provider", "forceColorScheme"),
#     Input("color-scheme-toggle", "n_clicks"),
#     State("mantine-provider", "forceColorScheme"),
#     prevent_initial_call=True,
# )
# def switch_theme(_, theme):
#     return "dark" if theme == "light" else "light"


@app.callback(
    Output("map-component", "children"),
    Input("submit_form_button", "n_clicks"),
    Input("get_data", "n_clicks"),
    State("place_name", "value"),
    State("address", "value"),
    State("description", "value"),
    State("rating", "value"),
    State("category", "value"),
    State("website", "value"),
    State("map-component", "children"),
    # prevent_initial_call=True,
    allow_duplicate=True,
)
def create_listing(n_clicks1, n_clicks2, place_name, address, desc, rating, category, website, map_items):
    ctx = callback_context
    button_clicked = ctx.triggered_id

    if button_clicked == "get_data":
        db = get_db("MontrealCompass")
        data = get_db_data(db, "listing_data")
        geojson = get_geo_data(data)
        return [dl.TileLayer(), dl.GeoJSON(data=geojson, cluster=True, zoomToBoundsOnClick=True, )]
    
    elif button_clicked == "submit_form_button":
        # TODO: make API call to get lat and lon
        new_listing_id = create_listing(db=db, place_name=place_name, address=address, latitude=0, longitude=0, description=desc, category=category, rating=rating, website=website)
        new_listing = get_one_listing(db, new_listing_id)
        map_items.append(new_listing)
        return map_items


if __name__ == "__main__":
    app.run_server(debug=True)
