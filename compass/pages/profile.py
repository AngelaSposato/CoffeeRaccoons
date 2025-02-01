from dash import html, register_page

title = "Profile"
register_page(
    __name__,
    path=f'/profile',
    page_components=[html.H1("My Profile"),],
)

layout = html.H2(title)