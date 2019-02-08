import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

#df = pd.DataFrame(data=['London', 'Bristol', 'Leeds', 'Manchester', 'Bath', 'Reading', 'Peterborough'], columns=['names'])
#data = [1,2,3,4,5,6,7]
#df['values'] = pd.DataFrame(data)
#df['city'] = df['names']
#df =df.set_index('names')

df = pd.read_csv('jobdata.csv')
df2 = df.groupby('locationName', as_index=False).agg({"applications":"sum", "jobId":"count"})
df2['locations'] = df2['locationName']
df2['ratio'] = df2['applications']/df2['jobId']

df2 = df2.sort_values(['applications'], ascending=False)
df2 = df2.set_index('locationName')

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        value=['London', 'central London', 'Birmingham', 'Manchester', 'Leeds', 'Bristol', 'Reading', 'Leicester', 'Nottingham', 'Sheffield'],
        options=[{'label': i, 'value': i} for i in df2['locations']],
        multi=True,
        id='dropdown'
    ),
    html.H3(id='output')
])

@app.callback(Output('output', 'children'), [Input('dropdown', 'value')])
def display_output(value):
    df_filtered = df2[df2["locations"].isin(value)]
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': list(flatten(df.loc[[input_data],['city']].values.tolist())) , 'y': list(flatten(df.loc[[input_data],['values']].values.tolist())), 'type': 'bar', 'name': 'city'},
                {'x':df_filtered['locations']  , 'y':df_filtered['ratio'] , 'type': 'line', 'name': 'ratio'},
            ],
            'layout': {
                'title': 'applications/jobs ratio'
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)

