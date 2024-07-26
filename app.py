# Import necessary libraries
from dash import Dash, html

# Create an instance of the Dash class
app = Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("Welcome to the Academic World Dashboard")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
