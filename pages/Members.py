import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H4("Hub Team"),
            html.A("HUB4SDG is a think tank, funded by IAPMEI StartUp Voucher 2020 program, with the objective to research "
                   "and develop a Sustainable Digital Platform for the monitorization, tracking and mitigation of potential "
                   "climate policy exchange in the short-term for the promotion of positive medium and long-term policy impact."),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H5("Climate Policy Unit (CPU)"),
            html.Br(),
            html.Br(),
            html.H6("Raul E. Fretes"),
            html.H5("Founder & Lead Promoter"),
            html.Img(src=app.get_asset_url("Raul.jpeg"), height="200px"),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H5("Environmental IT Unit (EITU)"),
            html.Br(),
            html.Br(),
            html.H6("Bruno Daniel Alho Fernandes"),
            html.H5("Co-Promoter & EITU Lead"),
            html.Img(src=app.get_asset_url("Raul.jpeg"), height="200px"),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H6("João Rafael Oliveira Simões"),
            html.H5("EITU Member"),
            html.Img(src=app.get_asset_url("Raul.jpeg"), height="200px"),
            html.Br(),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H6("Guilherme Costa Marques Lopes Simoes"),
            html.H5("EITU Member"),
            html.Img(src=app.get_asset_url("Gui.jpeg"), height="160px"),
            html.Br(),
        ])
    ]),
])