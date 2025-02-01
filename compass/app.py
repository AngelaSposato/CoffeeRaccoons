import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
from dash_iconify import DashIconify
from dash import html
import dash_leaflet as dl
from dash import Dash, _dash_renderer, Input, Output, State, callback

_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

map = dl.Map(dl.TileLayer(), center=[45.5019, -73.5674], zoom=6, style={'height': '50vh'})

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Montreal compass", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                dmc.Button("Add spot")
            ],
            p="md",
        ),
        dmc.AppShellMain(map),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)

app.layout = dmc.MantineProvider(layout)


@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)