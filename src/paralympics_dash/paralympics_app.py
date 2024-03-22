from dash import Dash, html
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

row_one = dbc.Row([
    dbc.Col([
        html.H1("Paralympics Dashboard"), html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
            "efficitur posuere metus posuere malesuada. ")
    ], width=12)
])

row_two = dbc.Row([
    dbc.Col(
        dbc.Select(
            options=[
                {"label": "Events", "value": "events"},
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",
            id="dropdown-input",
        ),
        width=2
    ),
    dbc.Col(
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        width=4
    ),
    dbc.Col(
        html.Div(
            [
                dbc.Label("Select the Paralympic Games type"),
                dbc.Checklist(
                    options=[
                        {"label": "Summer", "value": "summer"},
                        {"label": "Winter", "value": "winter"},
                    ],
                    value=["summer"],
                    id="checklist-input",
                ),
            ]
        ),
        width=2
    ),
    dbc.Col(
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid"),
        width=4
    ),
], align="start")

row_three = dbc.Row([
    dbc.Col(
        html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid"),
        width=8
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardImg(src="assets/logos/2022_Beijing.jpg", top=True, style={"width": "200px"}),
                dbc.CardBody(
                    [
                        html.H4("TownName 2026", className="card-title"),
                        html.P(
                            "Highlights of the paralympic event will go here. This will be a sentence or two.",
                            className="card-text",
                        ),
                        html.P(
                            "Number of athletes: XX",
                            className="card-text",
                        ),
                        html.P(
                            "Number of events: XX",
                            className="card-text",
                        ),
                        html.P(
                            "Number of countries: XX",
                            className="card-text",
                        ),
                    ]
                )
            ],
            style={"width": "18rem"},
        ), width=4),
], align="start")

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three
])

if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
