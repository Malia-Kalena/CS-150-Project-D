from dash import dcc, html
import dash_bootstrap_components as dbc
from assets.figures import correlation_heatmap

def tab2_layout(df):
    df_tab2 = df.copy()
    df_tab2['Inverted_Stress_Level'] = 10 - (df_tab2['Stress_Level'] + df_tab2['Daily_Screen_Time'] * 0.2 + df_tab2['App_Social_Media_Time'] * 0.3)
    df_tab2['Well_Being_Score'] = df_tab2['Daily_Screen_Time'] * 1.5 + 3
    df_tab2['Mood_Rating'] = df_tab2['App_Social_Media_Time'] * 1.1 + 1
    df_tab2_numeric = df_tab2.select_dtypes(include=['float64', 'int64'])
    corr_matrix = df_tab2_numeric.corr()
    print(corr_matrix.head(10))

    return dbc.Container(
        [
            html.Div(
                [
                    html.H3("📊 Irrefutable Science", className="mt-4"),
                    html.P("When in doubt, correlate.", className="mb-4"),
                    html.Hr()
                ],
                style={"textAlign": "center"},
            ),
            html.Div(
                dcc.Graph(figure=correlation_heatmap(df_tab2)),
                style={"display": "flex", "justifyContent": "center"}
            )
        ],
        fluid=True,
        style = {"padding": "20px"}
    )