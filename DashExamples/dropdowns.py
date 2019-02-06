import dash
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv('jobdata.csv')
df2 = df.groupby('locationName', as_index=False).agg({"applications":"sum", "jobId":"count"})
df2['locations'] = df2['locationName']
df2['ratio'] = df2['applications']/df2['jobId']

df2 = df2.sort_values(['applications'], ascending=False)
df2 = df2.set_index('locationName')



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Region"),
              dcc.Dropdown(
                  id="region-selector",
    options=[
        {'label': n, 'value': n} for n in df2['locations']
        #{'label': 'Montreal', 'value': 'MTL'},
        #{'label': 'San Francisco', 'value': 'SF'}
    ],
    placeholder="Select a city",
    multi=True,
    value = ["London", "Central London", "City of London", "City Of London", "Bristol", "Leeds"]
),
            ]
        ),
        html.Hr(),
        html.P(
            "Data from job boards.",
            className="text-muted",
        ),
    ],
    body=True,
)


app.layout = dbc.Container(
    [
        html.H1("Job application to job ratio by region"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id='example-graph'), md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

@app.callback(
    Output('example-graph',"figure"), [Input("region-selector", "value")]
    )

def make_graph(region):
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df2.loc[[region]], 'y': df2['ratio'], 'type': 'line', 'name': 'SF'},
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Applications/Job Ratio'
            }
        }
    )




if __name__ == '__main__':
    app.run_server(debug=True)