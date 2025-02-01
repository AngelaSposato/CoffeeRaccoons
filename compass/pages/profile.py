from dash import html, register_page
from components import map_component

title = "Profile"
register_page(
    __name__,
    path=f'/profile',
    page_components=[ ],
)

layout = html.H2(title)