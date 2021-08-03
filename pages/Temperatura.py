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
DATA_PATH = PATH.joinpath("../data/Temperatura/").resolve()
temp_media_pt = pd.read_csv(DATA_PATH.joinpath('Temperatura Media 1995-2020.csv'))
temp_max = pd.read_excel(DATA_PATH.joinpath('Temperatura máxima do mes mais quente do ano 1960-2020.xlsx'))
temp_media = pd.read_excel(DATA_PATH.joinpath('Temperatura média do ar 1995-2020.xlsx'))

#--------------- Interactive component --------------#

regioes = temp_max.drop(['Anos '],axis=1).columns.to_list()
anos = temp_media_pt[' Year'].unique()

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
            html.Label('Ano'),
            dropdown_year
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line_temp_portugal')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Estação Meteorológica'),
            dropdown_estacao
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar_plot_temp_media')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar_plot_temp_max')
        ])
    ])
])

#--------------- Callbacks --------------#
@app.callback(
    Output('bar_plot_temp_max','figure'),
    Input('estacao_drop','value')
)
def barplot_max(estacao):
    fig = px.bar(temp_max, x='Anos ', y=estacao, title="Temperatura máxima do mês mais quente do ano 1960-2020")
    fig.update(layout_coloraxis_showscale=False)
    return fig

@app.callback(
    Output('bar_plot_temp_media','figure'),
    Input('estacao_drop','value')
)
def barplot_media(estacao):
    fig = px.bar(temp_media, x='Anos ', y=estacao, title="Temperatura média 1995-2020")
    fig.update(layout_coloraxis_showscale=False)
    return fig

@app.callback(
    Output('line_temp_portugal','figure'),
    Input('year_drop','value')
)
def line_portugal(year):
    df = temp_media_pt[temp_media_pt[' Year']==year]
    fig = px.line(df, x=" Statistics", y="Temperature - (Celsius)", title='Temperatura média por mês 1995-2020')
    fig.update(layout_coloraxis_showscale=False)
    return fig