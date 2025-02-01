from dash import html, register_page
from components import map_component

register_page(
    __name__,
    path='/',
    page_components=[html.H1("Home"), html.P("Welcome to the Montreal Compass"), map_component],
)

layout = html.H2("Home page")