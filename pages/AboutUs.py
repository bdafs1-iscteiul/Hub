import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.Br(),
           html.H5("Empowering Policy and Decision-maker’s decisions"),
           html.A("HUB4SDG is an independent think tank working to innovate and fulfill climate policy by creating Monitore, "
                         "Report, and Evaluation (MRE) policy assessment instrument for climate policymakers and decision-makers with "
                         "residence in Lisbon, Portugal")
       ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H4("Work"),
            html.Br(),
            html.H5("Adaptable and Flexible Climate Policies with Real-Time"),
            html.A("Science declares that the global warming cap at 1.5°C is essential to avoid a climate catastrophe. "
                   "For having fighting chance at doing this, we must halve global emissions by 2030. Climate policy and actions "
                   "are the main instrument to ensure a sustainable and equal Climate Transition.")
        ])
    ]),
    dbc.Row([
       dbc.Col([
           html.Br(),
           html.H4("Goal"),
           html.Br(),
           html.H5("Foreseeing Policy outcomes in the short-term"),
           html.A("Our goal is to provide a predictive policy outcome algorithm to improve the "
                  "sustainable transition by 2050, with greater prosperity for all sectors through a Sustainable Digital Platform.")
       ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H5("What we Do"),
            html.A("Track policy: we monitor, challenge and help organizations to make policy flexible and adaptable "
                   "throughout its lifespan through our platform."),
            html.Br(),
            html.A("Calculate potential outcome: we monitor, asses and help "
                   "organizations to make their policy flexible and adaptable to climate variables and uncertainties throughout its lifespan."),
            html.Br(),
            html.A("Advice & Recommendations: We advise and challenge policy and decision-makers’ policy and actions to maxims their rate success and impact. We grow our networks."
                   "We join up organizations to unlock the power of collective climate policy portfolio of past, present and future actions.")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H5("How we Do It"),
            html.A("Dedicated Climate Policy Indicators:"),
            html.Br(),
            html.A("Past, Present & Future Data: "),
            html.Br(),
            html.A("Real-Time Data: we focus on promoting real-time climate data to predict policy outcome in the short-term "
                   "to maximize positive outcomes in the medium and long-term."),
            html.Br(),
            html.A("Collaboration: we share what we achieve together we partner organizations and vice-versa to take full "
                   "advantage institutional cooperation and knowledge sharing on climate change.")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Img(src=app.get_asset_url("fundosEuropeus.png"),height="130px"),
            html.Br()
        ])
    ])
])