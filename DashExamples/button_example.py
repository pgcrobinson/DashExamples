
import dash
import dash_html_components as html
import dash_core_components as dcc
from simple_html import example

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    #html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='url', href="/example"),
    dcc.Location(id='url', refresh=False),html.Div(id='page-content')
])


@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
    #[dash.dependencies.State('input-box', 'value')])
def display_page(pathname):
    return example,
    'The input value was "{}" and the button has been clicked {} times'.format(
        
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)