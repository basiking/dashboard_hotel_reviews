from dash import Dash, html, dcc, Input, Output, callback, State, dash_table
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__, title="BDS Assignment 2 Dashboard", suppress_callback_exceptions=True)
# Required dashboard items
# Overview of the entire collection
# Zoom in on items of interest
# Filter out interesting items or filter in interesting items
# Details on demand: select item or group and get relevant information accordingly
# At least 2 tabs

# Main app layout, tabs rendered by callback
app.layout = html.Div([
    html.H1('BDS Assignment 2'),
    dcc.Tabs(id='tabs-navigation', value='tab-1', children=[
        dcc.Tab(label='Tab 1: Algemeen', value='tab-1'),
        dcc.Tab(label='Tab 2: Voorspelling', value='tab-2'),
        dcc.Tab(label='Tab 3: Model Informatie', value='tab-3')
    ]),
    html.Div(id='tab-output')
])
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


@callback(Output('tab-output', 'children'),
          Input('tabs-navigation', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Algemene informatie'),
            html.Div([
                html.Div([
                    dcc.Graph(
                        figure=go.Figure(go.Bar(x=[1, 2, 3, 4], y=[10, 20, 30, 40]))
                    )
                ], className='graphTwoInARow'),
                html.Div([
                    dcc.Graph(
                        figure=go.Figure(go.Bar(x=[1, 2, 3, 4], y=[10, 20, 30, 40]))
                    )
                ], className='graphTwoInARow')
            ]),  # Top row
            html.Div([
                html.Div([
                    dcc.Graph(
                        figure=go.Figure(go.Bar(x=[1, 2, 3, 4], y=[10, 20, 30, 40]))
                    )
                ], className='graphThreeInARow'),
                html.Div([
                    dcc.Graph(
                        figure=go.Figure(go.Bar(x=[1, 2, 3, 4], y=[10, 20, 30, 40]))
                    )
                ], className='graphThreeInARow'),
                html.Div([
                    dcc.Graph(
                        figure=go.Figure(go.Bar(x=[1, 2, 3, 4], y=[10, 20, 30, 40]))
                    )
                ], className='graphThreeInARow')
            ]),  # Bottom row

        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Voorspelling maken'),
            html.Div([  # Top row
                html.Div([
                    dcc.Textarea(id='review-input-text'),
                    dcc.Dropdown(id='review-input-dropdown',
                                 className='reviewInputDropdown',
                                 options=['Model 1', 'Model 2', 'Model 3'],
                                 placeholder='Kies een model'),
                    dcc.Checklist(id='review-input-checkbox',
                                  className='dropdownChecklist',
                                  options=[{'label': 'Review opslaan in database?', 'value': 'save_review_in_db'}]),
                    html.Button(id='review-input-button', n_clicks=0, children='Analyzeer')
                ], className='predictionInputForm')  # Centered form
            ]),
            html.Div([  # Bottom row
                html.Div([
                    html.H4('Resultaat analyze van review'),
                ],
                    className='predictionOutputInformation',
                    id='prediction-output-information'),
                html.Div([
                    html.H4('Eerdere analyses'),
                    html.Div(id='previous-analyses',
                             className='previousAnalysesBox',
                             children=[dash_table.DataTable(df.to_dict('records'),
                                                            [{"name": i, "id": i} for i in df.columns])])
                ], className='previousPredictionsInfo',
                    id='previous-predictions-info'),  # Box containing previous stored predictions on left side
            ],
            )
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Model informatie'),
            html.Div(children=[
                html.H4('Model 1'),
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat eget lectus a commodo. Etiam "
                "a viverra tellus. Nullam dui risus, tristique vitae varius nec, faucibus vitae est. Quisque "
                "elementum, felis rhoncus dignissim lobortis, lacus ipsum pulvinar tellus, nec suscipit dui odio nec "
                "sapien. Etiam id fermentum nunc, nec aliquam magna. Curabitur tempus a dui non ultrices. Aliquam a "
                "congue nisi. Ut vestibulum ipsum eu feugiat cursus."
            ], className='graphThreeInARow'),
            html.Div(children=[
                html.H4('Model 2'),
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat eget lectus a commodo. Etiam "
                "a viverra tellus. Nullam dui risus, tristique vitae varius nec, faucibus vitae est. Quisque "
                "elementum, felis rhoncus dignissim lobortis, lacus ipsum pulvinar tellus, nec suscipit dui odio nec "
                "sapien. Etiam id fermentum nunc, nec aliquam magna. Curabitur tempus a dui non ultrices. Aliquam a "
                "congue nisi. Ut vestibulum ipsum eu feugiat cursus."
            ], className='graphThreeInARow'),
            html.Div(children=[
                html.H4('Model 3'),
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat eget lectus a commodo. Etiam "
                "a viverra tellus. Nullam dui risus, tristique vitae varius nec, faucibus vitae est. Quisque "
                "elementum, felis rhoncus dignissim lobortis, lacus ipsum pulvinar tellus, nec suscipit dui odio nec "
                "sapien. Etiam id fermentum nunc, nec aliquam magna. Curabitur tempus a dui non ultrices. Aliquam a "
                "congue nisi. Ut vestibulum ipsum eu feugiat cursus."
            ], className='graphThreeInARow')
        ])


@app.callback(Output('prediction-output-information', 'children'),
              Input('review-input-button', 'n_clicks'),
              State('review-input-text', 'value'),
              State('review-input-dropdown', 'value'),
              State('review-input-checkbox', 'value'),
              prevent_initial_call=True)
def analyse_user_review(button_click, user_review, model_chosen, save_to_db):
    print(f'user created review ({button_click}) ({user_review})')
    save_to_db = True if save_to_db is not None else False

    predicted_sentiment = 'Positive'
    prediction_accuracy = 90
    return html.Div(children=[
        html.H4('Resultaat analyze van review'),
        f'Model chosen: {model_chosen}',
        html.Br(),
        f'Save to db: {save_to_db}',
        html.Br(),
        f'Predicted sentiment: {predicted_sentiment}',
        html.Br(),
        f'Prediction accuracy: {prediction_accuracy}',
        html.Br(),
        'Prediction accurate?',
        html.Button('Yes', id='prediction-is-accurate'), html.Button('No', id='prediction-not-accurate')
    ])


# Start the dashboard
if __name__ == '__main__':
    app.run(debug=True)
