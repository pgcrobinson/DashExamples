import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from simple_html import example

external_stylesheets2 = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Nav([
    
        dbc.NavItem(dbc.NavLink( dbc.Button("Primary", color="primary"),active=True,href="/about"))
        #dcc.Link(html.Button('primary'), href="/about")
        #html.Button("Primary", color="primary", className="mr-1"), href="/about"
       
    
    #,pills=True,
])

if __name__ == '__main__':
    app.run_server(debug=True)