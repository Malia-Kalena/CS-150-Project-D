from dash import dcc, html
import pandas as pd
from assets.figures import time_series_chart, scatter_fig

def tab1_layout(df):
    df_tab1 = df.copy()
    df_tab1['Date'] = pd.to_datetime(df_tab1['Date'])
    df_tab1['Daily_Screen_Time'] = df_tab1['Daily_Screen_Time'] / 60
    df_tab1['Happiness_Index'] = (
        df_tab1['Well_Being_Score'] +
        df_tab1['App_Social_Media_Time'] * 0.3 -
        df_tab1['Stress_Level'] * 0.1
    )

    df_time_series = df_tab1.copy()
    df_time_series['Daily_Screen_Time'] = df_tab1['Daily_Screen_Time'] * 3 - 10
    df_time_series['Happiness_Index'] = df_time_series['Daily_Screen_Time'] * 3 - 10
    df_time_series['Month'] = df_tab1['Date'].dt.to_period('M').astype(str)

    df_tab1['Month'] = df_tab1['Date'].dt.to_period('M').astype(str)
    month_options = sorted(df_tab1['Month'].unique())

    return html.Div(
        [
            dcc.Store(id='data-store', data=df_time_series.to_dict('records')),
            html.Div(
                [
                    html.H3("🧠 The Truth in Trends", className="mt-4"),
                    html.P("Let's begin with the hard data.", className="mb-4"),
                    html.Hr()
                ],
                style={"textAlign": "center"}
            ),
            html.Div(
                [
                    dcc.Graph(
                        id='time-series-chart',
                        figure=time_series_chart(df_time_series),
                        style={"maxWidth": "80%", "margin": "0 auto"}
                    )
                ],
                className="mb-5"
            ),
            html.Div(
                [
                    html.P("Select a Month:",
                           style={
                               'fontSize': '20px',
                               'fontWeight': 'bold',
                               'textAlign': 'left',
                               'marginBottom': '10px',
                               'maxWidth': '80%',
                               'margin': '0 auto'
                           }),
                    html.Div(
                        dcc.Slider(
                            id='month-slider',
                            min=0,
                            max=len(month_options) - 1,
                            step=1,
                            marks={i: pd.to_datetime(month).strftime('%b %Y') for i, month in enumerate(month_options)},
                            value=0,
                            included=False,
                            updatemode='drag',
                            tooltip={"placement": "bottom", "always_visible": False},
                        ),
                        style={
                            'margin': '0 auto',
                            'width': '60%',
                        }
                    )
                ],
                className="mb-5"
            ),
            html.Div(
                [
                    html.Hr(),
                    dcc.Graph(
                        id='scatter-plot',
                        figure=scatter_fig(df_tab1),
                        style={"maxWidth": "80%", "margin": "0 auto"}
                    )
                ],
                className="mb-5"
            )
        ],
        style={"padding": "20px"}
    )
