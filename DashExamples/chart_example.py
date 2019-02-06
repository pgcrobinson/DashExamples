import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis data'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[4, 5, 6],
    name='yaxis2 data',
    yaxis='y2'
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),



dcc.Graph(
    figure=go.Figure(
        data=[
            trace1, trace2 ],
  layout = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='yaxis title'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
    ),
    style={'height': 300},
    id='my-graph'
)
])



if __name__ == '__main__':
    app.run_server(debug=True)