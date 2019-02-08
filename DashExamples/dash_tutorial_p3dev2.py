import pandas_datareader.data as web
import datetime
import dash
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from more_itertools import flatten

df = pd.DataFrame(data=['London', 'Bristol', 'Leeds', 'Manchester', 'Bath', 'Reading', 'Peterborough'], columns=['names'])
data = [1,2,3,4,5,6,7]
df['values'] = pd.DataFrame(data)
df['city'] = df['names']
df =df.set_index('names')
#print(df['city'].tolist())
#print(df.loc[['London','Bristol'],['city']].values.tolist())
#a = df.loc[['London','Bristol'],['city']].values.tolist()
#print(list(flatten(df.loc[['London','Bristol'],['city']].values.tolist())))
#print(df.loc[['London','Bristol'],['city']])

#df_filtered = df[df['city']=='London']
#print(df_filtered['values'])


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Finance'),



    html.Div(children='''
        Stock Prices
    '''),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': n, 'value': n} for n in df['city']
            
            ],
        #multi=True,
        value='London'),
    html.Div(id='output-graph')

    
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
    )
def update_graph(input_data):
    #start= datetime.datetime(2015,1,1)
    #end=datetime.datetime.now()
    df_filtered = df[df['city']==input_data]
    #df = web.DataReader(input_data, 'iex', start, end)
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': list(flatten(df.loc[[input_data],['city']].values.tolist())) , 'y': list(flatten(df.loc[[input_data],['values']].values.tolist())), 'type': 'bar', 'name': 'city'},
                {'x':df_filtered['city']  , 'y':df_filtered['values'] , 'type': 'bar', 'name': 'city'},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)


