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
DATA_PATH = PATH.joinpath("../data/Precipitaçoes/").resolve()
estaçoes_metriologicas = pd.read_excel(DATA_PATH.joinpath('Precipitação 1991-2020.xlsx'))
portugal = pd.read_csv(DATA_PATH.joinpath('Precipitaçoes Portugal.csv'))

#--------------- Interactive component --------------#

regioes = estaçoes_metriologicas.drop(['Anos ','Unnamed: 10'],axis=1).columns.to_list()
anos = portugal[' Year'].unique()

estacao_options = [dict(label = regiao, value = regiao) for regiao in regioes]
year_options = [dict(label = year, value = year) for year in anos ]

dropdown_estacao = dcc.Dropdown(
    id = 'estacao_drop',
    options=estacao_options,
    value='Lisboa',
    multi= False
)

dropdown_year = dcc.Dropdown(
    id = 'year_drop',
    options= year_options,
    value= 1991,
    multi= False
)
#--------------- Layout --------------#
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label('Estação Meteorológica'),
            dropdown_estacao
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar_plot_p')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Ano'),
            dropdown_year
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='precipitaçao_portugal')
        ])
    ])
])

#--------------- Callbacks --------------#
@app.callback(
    Output('bar_plot_p','figure'),
    Input('estacao_drop','value')
)
def barplot(estacao):
    fig = px.bar(estaçoes_metriologicas, x='Anos ', y=estacao, title="Precipitação de 1991 até 2020")
    fig.update(layout_coloraxis_showscale=False)
    return fig

@app.callback(
    Output('precipitaçao_portugal','figure'),
    Input('year_drop','value')
)
def line_portugal(year):
    df = portugal[portugal[' Year']==year]
    fig = px.line(df, x=" Statistics", y="Rainfall - (MM)", title='Precipitação por meses em Portugal')
    fig.update(layout_coloraxis_showscale=False)
    return fig