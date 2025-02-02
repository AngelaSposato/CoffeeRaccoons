import dash_leaflet as dl
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


MOON_ICON = DashIconify(icon="radix-icons:moon", width=25)
SUN_ICON = DashIconify(icon="radix-icons:sun", width=25)


theme_toggle = dmc.ActionIcon(
    [
        dmc.Paper(SUN_ICON, darkHidden=True),
        dmc.Paper(MOON_ICON, lightHidden=True),
    ],
    variant="transparent",
    color="yellow",
    id="color-scheme-toggle",
    size="lg",
)


map_component = dl.Map(
    children=[],
    center=[45.5019, -73.5674],
    zoom=11,
    style={"height": "50vh"},
    id="map-component",
)

button = dmc.Button(children="Get Data", id="get_data")

place_name = dmc.TextInput(
    placeholder="Enter the name of the place",
    label="Name",
    id="place_name",
    radius="md",
    required=True,
    mt=10,
)

address = dmc.TextInput(placeholder="Enter the address", label="Address", id="address", radius="md", mt=10, required=True)

rating = dmc.Rating(id="rating", mt=10, size="lg")

description = dmc.TextInput(
    placeholder="Enter a description for this place",
    label="Description",
    id="description",
    radius="md",
    required=True,
    mt=10,
)

category = dmc.TagsInput(
    label="Select categories",
    id="category",
    description="You can select a maximum of 3 categories.",
    maxTags=3,
    splitChars=[",", " ", "|"],
    data=[
        "Restaurant",
        "Bar",
        "Cafe",
        "Park",
        "Museum",
        "Theatre",
        "Store",
        "Library",
        "Gym",
        "Hotel",
        "Other",
    ],
    w=400,
    mt=10,
    required=True,
)

website = dmc.TextInput(
    placeholder="Enter the website/socials for this place",
    label="Website",
    id="website",
    radius="md",
    required=True,
    mt=10,
)

submit_form_button = dmc.Button(
    "Submit",
    loaderProps={"type": "dots"},
    loading=False,
    id="submit_form_button",
    size="sm",
    radius="md",
    mt=20,
)

listing_form = dmc.Fieldset(
    children=[place_name, address, description, category, rating, website, submit_form_button],
    legend="Create a listing",
    id="listing_form",
    mt=20,
    mr=10,
    ml=10,
    variant="filled",
    radius="md",
)

data_display = dmc.Container([dmc.Textarea(id="data_display", readOnly=True)], mt=20)

layout = dmc.MantineProvider(
    id="mantine-provider", forceColorScheme="light", children=[listing_form, data_display]
)
