import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import pathlib
from app import app

#--------------- Importing --------------#
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data/Eventos Extremos/").resolve()
grau_area_ardida = pd.read_excel(DATA_PATH.joinpath('Grau de area ardida.xlsx'))
incendios_rurais = pd.read_excel(DATA_PATH.joinpath('Incendios rurais e area ardida.xlsx'))
totais =  pd.read_excel(DATA_PATH.joinpath('totais 2001-2010.xlsx'))

#--------------- Interactive component --------------#
anos = grau_area_ardida['Anos'].unique()
tipo_incendios_rurais = ['Total Incendios','Florestais']
tipo_area_rural = ['Total Area Ardida','Povoamentos florestais','Matos','Agrícola']
numero_ocorrencias = ['Fogachos','Incêndios','Total']
area_ardida = ['Povoamento','Mato','EspaçoFlorestal (pov+mato)']

ocorrencias_options = [dict(label = tipo, value = tipo) for tipo in numero_ocorrencias ]
area_ardida_options = [dict(label = tipo, value = tipo) for tipo in area_ardida ]
area_rural_options = [dict(label = tipo, value = tipo) for tipo in tipo_area_rural ]
incendios_options = [dict(label = tipo, value = tipo) for tipo in tipo_incendios_rurais ]
year_options = [dict(label = year, value = year) for year in anos ]

dropdown_year = dcc.Dropdown(
    id = 'year_drop',
    options= year_options,
    value= 2001,
    multi= False
)

dropdown_incendio_rural = dcc.Dropdown(
    id = 'incendios_rurais',
    options= incendios_options,
    value= 'Total Incendios',
    multi= False
)

dropdown_area_ardida_rural = dcc.Dropdown(
    id = 'area_rural',
    options= area_rural_options,
    value= 'Total Area Ardida',
    multi= False
)

dropdown_numero_ocorrencias = dcc.Dropdown(
    id = 'numero_ocorrencias',
    options= ocorrencias_options,
    value= 'Total',
    multi= False
)

dropdown_area_ardida = dcc.Dropdown(
    id = 'area_ardida',
    options= area_ardida_options,
    value= 'EspaçoFlorestal (pov+mato)',
    multi= False
)

#--------------- Layout --------------#
layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.Label('Ano'),
           dropdown_year
       ]),
       dbc.Col([
           dbc.Card([
               dbc.CardBody([
                   html.H4('Grau de Area Ardido', className='text-white'),
                   html.Br(),
                   dbc.ListGroup([
                       dbc.ListGroupItem(id='grau_ardido')
                   ])
               ])
           ], color="#363636", className='mb-2 mt-3', style={"height": 155})
       ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Tipo de Incendio Rural'),
            dropdown_incendio_rural
        ]),
        dbc.Col([
            html.Label('Tipo de Area Rural'),
            dropdown_area_ardida_rural
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='rural')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Tipo de Ocurrencia'),
            dropdown_numero_ocorrencias
        ]),

        dbc.Col([
            html.Label('Tipo de Area Ardida'),
            dropdown_area_ardida
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='nacional')
        ])
    ])
])

#--------------- Callbacks --------------#
@app.callback(
    Output('rural','figure'),
    [Input('incendios_rurais','value'),
     Input('area_rural','value')]
)
def rural(incendio,area):
    incendio = dict(type='scatter', x=incendios_rurais['Anos'], y=incendios_rurais[incendio], name='Numero de Ocurrencias')
    area_rural = dict(type='bar', x=incendios_rurais['Anos'], y=incendios_rurais[area], name='Area Ardida (Hectares)')
    data = [incendio, area_rural]
    layout = dict(title=dict(text='Numero de Incendios rurais e Area Ardida (Hectares)'), xaxis=dict(title='Anos'))
    return go.Figure(data=data, layout=layout)

@app.callback(
    Output('nacional','figure'),
    [Input('numero_ocorrencias','value'),
     Input('area_ardida','value')]
)
def total(ocurrencias,area):
    incendio = dict(type='scatter', x=totais['Ano'], y=totais[ocurrencias], name='Numero de Ocurrencias')
    area_rural = dict(type='bar', x=totais['Ano'], y=totais[area], name='Area Ardida (Hectares)')
    data = [incendio, area_rural]
    layout = dict(title=dict(text='Numero de Ocurrencias e Area Ardida (Hectares)'), xaxis=dict(title='Anos'))
    return go.Figure(data=data, layout=layout)

@app.callback(
    Output('grau_ardido', 'children'),
    Input('year_drop','value')
)
def indicators(year):
    grau = grau_area_ardida[grau_area_ardida.Anos == year]['Grau de área ardida'].values[0]
    return str(grau)
