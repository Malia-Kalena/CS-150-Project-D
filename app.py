from dash import dcc, html, Input, Output, State, dash
import dash_bootstrap_components as dbc
import pandas as pd
import dash
import random

from assets.figures import time_series_chart
from tabs.tab1 import tab1_layout
from tabs.tab2 import tab2_layout
from tabs.tab3 import tab3_layout, generate_super_fun_message
from tabs.tab4 import tab4_layout

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME],
)

df = pd.read_csv("assets/mental_health_screen_time_dataset.csv")

footer = html.Div(
    dcc.Markdown(
        """
         This information is 100% true and the real deal. You can substitute this for
          professional advice if needed.
          DATA SOURCE: https://www.kaggle.com/datasets/yajkotak/mental-health-and-screen-time-correlation-dataset
        """
    ),
    style={"backgroundColor": "#4a90e2", "color": "white", "padding": "0.5rem", "marginTop": "2rem",
           "fontSize": "small"},
)

"""
===========================================================================
Main Layout
"""

app.layout = html.Div(
    [
        html.Div(
            [
                # Title
                html.H1(
                    "📲 12 Hours a Day Keeps the Therapist Away!👩‍⚕️",
                    style={'textAlign': 'center',
                           'color': 'white',
                           'margin': '0',
                           'padding': '20px'
                    }
                ),
                html.P(
                    "by Malia de Jesus (CS-150)",
                    style = {'textAlign': 'center',
                             'color': 'white',
                             'margin': '0',
                             'padding': '10px'
                    }
                ),
            ],
            style={
                'backgroundColor': '#4a90e2',
                'width': '100%',
                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                'marginBottom': '20px',
            }
        ),

        # Tabs
        dcc.Tabs(
            id='tabs',
            value='tab-1',
            children=[
                dcc.Tab(label='1: Truth in Trends', value='tab-1'),
                dcc.Tab(label='2: Irrefutable Science', value='tab-2'),
                dcc.Tab(label='3: Predict Your Happiness', value='tab-3'),
                dcc.Tab(label='4: FAQ', value='tab-4'),
            ],
            style={'fontWeight': 'bold'}
        ),
        html.Div(id='tabs-content'),
        dbc.Row(dbc.Col(footer)),
    ],
    style={"padding": "20px"}
)



"""
==========================================================================
Callbacks
"""

@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tabs):
    if tabs == 'tab-1':
        return tab1_layout(df)
    elif tabs == 'tab-2':
        return tab2_layout(df)
    elif tabs == 'tab-3':
        return tab3_layout()
    elif tabs == 'tab-4':
        return tab4_layout()


@app.callback(
    Output('time-series-chart', 'figure'),
    Input('month-slider', 'value'),
    State('data-store', 'data')
)
def update_time_series_chart(month_index, data):
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure datetime for filtering
    df['Month'] = df['Date'].dt.to_period('M').astype(str)

    unique_months = sorted(df['Month'].unique())
    selected_month = unique_months[month_index]

    filtered_df = df[df['Month'] == selected_month]

    # Group by day for line chart
    daily_avg = filtered_df.groupby('Date').agg({
        'Daily_Screen_Time': 'mean',
        'Happiness_Index': 'mean'
    }).reset_index()

    return time_series_chart(daily_avg)



@app.callback(
    Output('screen-time-slider', 'value'),
    Output('prediction-output', 'children'),
    Input('screen-time-slider', 'value'),
    Input('lucky-button', 'n_clicks'),
    prevent_initial_call='initial_duplicate'
)
def update_prediction(screen_time, n_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        triggered_input = None
    else:
        triggered_input = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_input == 'lucky-button':
        screen_time = round(random.uniform(0, 25), 1)

    prediction = generate_super_fun_message(screen_time)
    return screen_time, prediction



@app.callback(
    Output('share-button', 'children'),
    Input('share-button', 'n_clicks')
)
def share_results(n_clicks):
    if n_clicks > 0:
        return "Shared! 📤 (Sike... not really)"
    return "Share Your Results 💖✨"



if __name__ == '__main__':
    app.run(debug=True)