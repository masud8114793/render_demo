# Import packages
from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server

df1 = px.data.gapminder()


main_body = dbc.Container([

    dbc.Row([
        dbc.Col(html.H1("My Bootstrap Dash App"), width=12,style={'textAlign': 'center'})
    ]),
    dbc.Row([
        dbc.Col(dash_table.DataTable(data=df.to_dict('records'), page_size=10), width=6),
        dbc.Col(dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')), width=6)
    ]),
    dbc.Card([
        dbc.CardHeader("Dashboard"),
        dbc.CardBody([
            dash_table.DataTable(data=df.to_dict('records'), page_size=10)
        ])
    ]),
    dbc.Card([
        dbc.CardHeader("Dashboard"),
        dbc.CardBody([
            dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
        ])
    ])
])

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src="/assets/logo.png", height="30px")),
                dbc.Col(dbc.NavbarBrand("My App", className="ms-2")),
            ], align="center", className="g-0"),
            href="/",
            style={"textDecoration": "none"},
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav([
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Reports", href="/reports", active="exact"),
                dbc.DropdownMenu(
                    [dbc.DropdownMenuItem("Settings", href="/settings"),
                     dbc.DropdownMenuItem("Help", href="/help")],
                    label="More",
                    nav=True,
                ),
            ], className="ms-auto", navbar=True),
            id="navbar-collapse",
            navbar=True,
        ),
    ]),
    color="dark",
    dark=True,
)


app.layout = html.Div([navbar, html.Div(id="page-content")])
app.layout = html.Div([main_body])

