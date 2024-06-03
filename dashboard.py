from dash import Dash, html

app = Dash()
# Required dashboard items
# Overview of the entire collection
# Zoom in on items of interest
# Filter out interesting items or filter in interesting items
# Details on demand: select item or group and get relevant information accordingly

# Main app layout
app.layout = [
    html.H1('BDS Assignment deel 2')
]


# Start the dashboard
if __name__ == '__main__':
    app.run(debug=True)
