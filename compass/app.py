from dash import Dash
import dash_mantine_components as dmc
import dash_leaflet as dl
from dash_extensions.pages import setup_page_components
from dash import Dash,  html, dcc, page_container,  page_registry

app = Dash(__name__, title='Montreal Compass', use_pages=True)

links = [html.Div(dcc.Link(p["name"], href=p["path"])) for p in page_registry.values()]

app.layout = dmc.MantineProvider(
    children=[
        page_container,  # page layout is rendered here
        setup_page_components(),  # page components are rendered here
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)