from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Interactive Line Graph"),

    # X-coordinate input section
    html.Div([
        html.Label("Enter X coordinates (comma-separated):", className="form-label"),
        dcc.Input(id='x-coordinates', type='text', value='1,2,3', className="form-control"),
    ]),

    # Y-coordinate input section
    html.Div([
        html.Label("Enter Y coordinates (comma-separated):", className="form-label"),
        dcc.Input(id='y-coordinates', type='text', value='2,3,5', className="form-control"),
    ]),

    # Plot button
    html.Button('Plot', id='plot-button', n_clicks=0, className="plot-btn"),

    # Graph display area
    dcc.Graph(id='line-graph', style={"height": "70vh"}),  # Set graph height to 70% of the viewport height
])

# Callback to update the graph based on user inputs
@app.callback(
    Output('line-graph', 'figure'),
    [Input('plot-button', 'n_clicks')],
    [Input('x-coordinates', 'value'),
     Input('y-coordinates', 'value')]
)

def update_graph(n_clicks, x_values, y_values):
    if n_clicks > 0:
        # Convert the comma-separated input values to a list of floats
        x = list(map(float, x_values.split(',')))
        y = list(map(float, y_values.split(',')))

        # Create the line graph
        trace = go.Scatter(x=x, y=y, mode='lines+markers', name='Line Plot', line=dict(color='blue'))
        layout = go.Layout(
            title='User-Defined Line Graph',
            xaxis=dict(title='X-axis'),
            yaxis=dict(title='Y-axis'),
            plot_bgcolor='rgba(255, 255, 255, 0.8)',  # White background
            paper_bgcolor='rgba(240, 240, 240, 0.9)',  # Light grey plot area
        )
        return {'data': [trace], 'layout': layout}
    else:
        # Initial empty graph when the page loads
        return {'data': [], 'layout': go.Layout(title='User-Defined Line Graph')}

# Start the Dash server
if __name__ == '__main__':
    app.run_server(debug=True)