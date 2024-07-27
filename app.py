# Import necessary libraries
from dash import Dash, html, dcc, Input, Output
from mysql_utils import get_top_universities

# Create an instance of the Dash class
app = Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("Welcome to the Academic World Dashboard"),
    dcc.Input(id='keyword-input', type='text', placeholder='Enter keyword'),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-div')
])

# Callback to update the output based on the input keyword
@app.callback(
    Output('output-div', 'children'),
    [Input('submit-button', 'n_clicks')],
    [Input('keyword-input', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks > 0 and value:
        results = get_top_universities(value)
        return html.Ul([html.Li(f"{res[0]}: {res[1]} publications") for res in results])
    return "Enter a keyword and press Submit"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
