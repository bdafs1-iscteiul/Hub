import dash_html_components as html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.H6("Adaptable policies",className='ml-5'),
            html.H6("Our Project", className='ml-5'),
        ],width=3),
        dbc.Col([
            html.A("Endorsing net-positive climate policies outcomes are complex and ambitious goals to obtain: first, "
                   "because their effects will have ever-lasting impacts across all-sectors; second, because as climate change "
                   "alters our environments, so will it hinder it’s counter-policies; lastly, Our project involves developing a "
                   "Sustainable Digital Platform to manage, develop studies and track climate policies and actions to mitigate "
                   "it’s potential Climate Exchange. ""Promoting, among policymaker, decision-makers, and policy influencers, "
                   "for sensorial policy assesment to adapt to socio-climate and enviromental uncertainty throughout it’s "
                   "life-cycle.")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.H6("Why a climate policies platform?",className='ml-1'),
        ], width=3),
        dbc.Col([
            html.Br(),
            html.A("Current policies would result in a 2.9°C rise by 2100, Climate Action Tracker "
                   "(Climate Analytics and NewClimate Institute). As seen on May 13, 2020 were Portugal exhausted the resources "
                   " that the country has the capacity to regenerate in a period of one year. (Global Footprint Network).")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.H6("Numbers don´t lie", className='ml-1'),
            html.H6("1 in 4 cities lack policies", className='ml-1'),
        ], width=3),
        dbc.Col([
            html.Br(),
            html.A("Nearly half of cities lack plans to keep populations safe from climate threats. 43% of global cities do not have "
                   "adaptation plans to keep people and critical infrastructure safe from climate threats. 93% of the 812 disclosing "
                   "cities report that they are at risk from climate change (CDP Cities Report 2020).")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.H6("Does Portugal climate work?", className='ml-1'),
            html.H6("3 in 10 territories outside of plans", className='ml-1'),
        ], width=3),
        dbc.Col([
            html.Br(),
            html.A("Depite Portuguese respondents consider climate change to be a very serious problem (87%), higher than the EU"
                   " average of 79% and been among the best EU Members agaist climate change.Eurobarometer Report 2019, European "
                   "CommissionPortugal’s CCPI ranking (17º rank) has led to the laid back of climate ambition resulting in been "
                   "between the worst EU Members on the Green Transition (PPR) and leaving almost a third of its territory out "
                   "of its national climate change plans and ZERO 2020 & ANP/WWF 2021")
        ])
    ])
])