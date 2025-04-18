from dash import dcc, html
import dash_bootstrap_components as dbc

def generate_super_fun_message(screen_time):
    mood = round(3 + (screen_time * 0.7), 1)
    stress = round(5 - (screen_time * 0.4), 1)
    well_being = round(50 + (screen_time * 5), 1)

    if screen_time < 2:
        msg = "I know. You're extremely stressed because you haven't scrolled today! Tsk tsk 😤... amateur behavior."
    elif screen_time < 5:
        msg = "Quite mild exposure to social media. Mood lifting 🌥️⛅🌤️... slooooowwwlyyy."
    elif screen_time < 9:
        msg = "Congrats! You've entered 💡Optimal Distraction Zone™💡. Dopamine activate."
    elif screen_time < 12:
        msg = "Double digits?!? Stress?? Don't know her. TikTok has healed your inner child ️🧘‍♀️"
    else:
        msg = "Exceptional work! You're 1) stress-free and 2) emotionally numb. That's what we call balance ⚖️"

    return (
        f"At {screen_time} hours:\n"
        f"😄 Mood: {mood}/10\n"
        f"😵 Stress: {stress}\n"
        f"💛 Well-Being: {well_being}/100\n"
        f"\n{msg}"
    )

def tab3_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.H3("🎰 Predict Your Happiness", className="mt-4"),
                    html.P("One slider to rule your mental state ❤️", className="mb-4"),
                    html.Hr(),
                ],
                style={"textAlign": "center"},
            ),

            html.Label("Select your daily screen time (hrs): "),
            dcc.Slider(
                id='screen-time-slider',
                min=0,
                max=24,
                step=0.5,
                value=0,
                marks={i: f'{i}h' for i in range(0, 25)},
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Br(),
            html.Div(
                [
                    html.Div(
                        id='prediction-output',
                        style={'whiteSpace': 'pre-line',
                               'fontFamily': 'monospace'
                               }
                    ),
                    html.Br(), html.Br(),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Button("🎲 Feeling Lucky",
                                            id="lucky-button",
                                            n_clicks=0,
                                            className="btn btn-primary w-100"
                                ),
                                width=3,
                                className="mb-2"
                            ),
                            dbc.Col(
                                html.Button("📤 Share Your Results",
                                            id="share-button",
                                            n_clicks=0,
                                            className="btn btn-secondary w-100"
                                ),
                                width=3
                            )
                        ],
                        justify="center"
                    ),
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                            "*The share button actually does nothing but you feel cool for clicking it.*",
                                 style={"textAlign": "center",
                                        "fontStyle": "italic",
                                        "marginTop": "0.5rem"
                                 }
                            ),
                            width="auto"
                        ),
                        justify="center"
                    ),
                ],
                style={"textAlign": "center"},
            )
        ],
        style = {"padding": "20px"}
    )