import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app

#--------------- Importing --------------#
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data/Emissoes/").resolve()
emissoes = pd.read_excel(DATA_PATH.joinpath('Emissoes.xlsx'))

gas_names = emissoes.drop('Anos',axis=1).columns.to_list()

anos = emissoes.Anos.values
#--------------- Interactive component --------------#

type_of_gas = [dict(label = gas, value = gas) for gas in gas_names]
year_options = [dict(label = year, value = year) for year in anos ]

dropdown_gas = dcc.Dropdown(
    id = 'gas_drop',
    options=type_of_gas,
    value='Dióxido de carbono de origem fóssil',
    multi= False
)

dropdown_year = dcc.Dropdown(
    id = 'year_drop',
    options= year_options,
    value= 1995,
    multi= False
)

#--------------- Layout --------------#
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label('Tipo de Gás'),
            dropdown_gas,
        ]),
        dbc.Col([
            html.Label('Ano'),
            dropdown_year
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dióxido de carbono de origem fóssil',className='text-white'),
                    dbc.ListGroup([
                        dbc.ListGroupItem(id='CO2Fossil')
                    ])
                ])
            ],color="#363636",className='mb-2 mt-3',style={"height":155})
        ],width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dióxido de carbono com origem na Biomassa', className='text-white'),
                    dbc.ListGroup([
                        dbc.ListGroupItem(id='CO2Bio')
                    ])
                ])
            ], color="#363636", className='mb-2 mt-3',style={"height":155})
        ],width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Metano', className='text-white'),
                    html.Br(),
                    dbc.ListGroup([
                        dbc.ListGroupItem(id='metano')
                    ])
                ])
            ], color="#363636", className='mb-2 mt-3',style={"height":155})
        ],width=4)
    ]),

    dbc.Row([
        dbc.Col([
                dcc.Graph(id='bar_plot')
        ],width=12)
    ])

])

#--------------- Callbacks --------------#
@app.callback(
    Output('bar_plot', 'figure'),
    [Input('gas_drop','value')]
)
def bar(gas):
    fig = px.bar(emissoes, x='Anos', y=gas,title="Emissões emitidas de 1995 até 2018")
    fig.update(layout_coloraxis_showscale=False)
    return fig


@app.callback(
    [Output('CO2Fossil', 'children'),
     Output('CO2Bio','children'),
     Output('metano','children')],
    [Input('year_drop','value')]
)
def indicators(year):
    co2fossil = emissoes.loc[emissoes['Anos'] == year][gas_names[0]].values[0]
    co2bio = emissoes.loc[emissoes['Anos'] == year][gas_names[1]].values[0]
    metano = emissoes.loc[emissoes['Anos'] == year][gas_names[2]].values[0]

    return str(co2fossil),\
            str(co2bio),\
            str(metano)