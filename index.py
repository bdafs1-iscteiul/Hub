import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from pages import Emissoes,EventosExtremos,AboutUs,Precipitacoes,Temperatura,Contact,Members,TheProject,UnderConstruction
from app import server


nav_item_about_us = dbc.NavItem(dbc.NavLink("About Us ", href="/AboutUs", active="exact"))
nav_item_project = dbc.NavItem(dbc.NavLink("The Project", href="/TheProject", active="exact"))
nav_item_members = dbc.NavItem(dbc.NavLink("Members ", href="/Members", active="exact"))
nav_item_contact = dbc.NavItem(dbc.NavLink("Contact ", href="/Contact", active="exact"))

dropdown_nav = dbc.DropdownMenu([
    dbc.DropdownMenuItem("Area of Focus ", header=True),
    dbc.DropdownMenuItem("Emissions", href="/Emissions"),
    dbc.DropdownMenuItem("Extreme Events", href="/ExtremeEvents"),
    dbc.DropdownMenuItem("Precipitations", href="/Precipitations"),
    dbc.DropdownMenuItem("Temperature", href="/Temperature")

],label='Area of Focus',color="#363636", nav=True, in_navbar=True,className='text-white')

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row([
                   html.A("HUB")
                ],className='text-white ml-3'),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item_about_us, dropdown_nav, nav_item_project, nav_item_members, nav_item_contact],
                    className="ml-5 text-white",
                    navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ], fluid=True,
    ),
    color="#363636",
    dark=True,
    className="mb-2 mr-0",
)

content = html.Div(id="page-content")

app.layout = html.Div(
    [dcc.Location(id="url"), logo, content],
)

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return UnderConstruction.layout
    elif pathname == '/ExtremeEvents':
        return EventosExtremos.layout
    elif pathname == '/Precipitations':
        return Precipitacoes.layout
    elif pathname == '/Temperature':
        return Temperatura.layout
    elif pathname == '/Emissions':
        return Emissoes.layout
    elif pathname == '/AboutUs':
        return AboutUs.layout
    elif pathname == '/TheProject':
        return TheProject.layout
    elif pathname == '/Members':
        return Members.layout
    elif pathname == '/Contact':
        return Contact.layout


if __name__ == '__main__':
    app.run_server(debug=True)
