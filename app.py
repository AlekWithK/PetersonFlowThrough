from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_parquet('Merges/PETERSON_MASTER.parquet').sample(n=100000)

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.datetime.dt.year.unique(), '1994', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.datetime.dt.year==value]
    return px.scatter(dff, x='datetime', y='chlor')

if __name__ == '__main__':
    app.run(debug=True)