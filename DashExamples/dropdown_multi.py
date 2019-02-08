import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

df = pd.DataFrame(data=['London', 'Bristol', 'Leeds', 'Manchester', 'Bath', 'Reading', 'Peterborough'], columns=['names'])
data = [1,2,3,4,5,6,7]
df['values'] = pd.DataFrame(data)
df['city'] = df['names']
df =df.set_index('names')

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        value=['London'],
        options=[{'label': i, 'value': i} for i in df['city']],
        multi=True,
        id='dropdown'
    ),
    html.H3(id='output')
])

@app.callback(Output('output', 'children'), [Input('dropdown', 'value')])
def display_output(value):
    df_filtered = df[df["city"].isin(value)]
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': list(flatten(df.loc[[input_data],['city']].values.tolist())) , 'y': list(flatten(df.loc[[input_data],['values']].values.tolist())), 'type': 'bar', 'name': 'city'},
                {'x':df_filtered['city']  , 'y':df_filtered['values'] , 'type': 'bar', 'name': 'city'},
            ],
            'layout': {
                'title': value
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
