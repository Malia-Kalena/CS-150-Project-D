import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

def time_series_chart(df):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Daily_Screen_Time'],
            name='Daily Screen Time (hrs)',
            yaxis='y1',
            line=dict(color='royalblue'),
            marker = dict(
                color='gray',  # Set color of markers
                size=8,  # Marker size
                line=dict(width=1, color='gray')  # Border color for markers
            ),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Happiness_Index'],
            name='Happiness Index',
            yaxis='y2',
            line=dict(color='limegreen'),
            marker = dict(
                color='gray',  # Set color of markers
                size=8,  # Marker size
                line=dict(width=1, color='gray')  # Border color for markers
            ),
        )
    )

    fig.update_layout(
        title="📈 Screen Time Makes Us Happy: The Totally Reliable Truth",
        font=dict(color='gray'),
        xaxis=dict(
            title='Date',
            ticks='outside',  # Ensure x-axis ticks show inside
            showline=True,
            linecolor='gray',
        ),
        yaxis=dict(
            title=dict(text='Screen Time (hrs)', font=dict(color='gray')),
            range=[0, 12],
            ticks='outside',  # Ensure y1 axis ticks show inside
            showticklabels=True,
            showline=True,
            linecolor='gray',
        ),
        yaxis2=dict(
            title=dict(text='Happiness Index', font=dict(color='gray')),
            range=[0, 20],  # Ensuring fixed range for the second axis
            ticks='outside',  # Ensure y2 axis ticks show inside
            anchor='x',  # Ensures y2 is aligned with the x-axis
            overlaying='y',  # Overlay y2 on top of y1 axis
            side='right',  # Position y2 on the right side
            showticklabels=True,
            showline=True,
            linecolor='gray',
        ),
        legend=dict(x=0.8, y=0.01),
        margin=dict(l=40, r=40, t=60, b=40),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return fig



def scatter_fig(df):
    # Separate screen time groups
    df_under_9 = df[df['Daily_Screen_Time'] < 7.5].dropna().sample(50, random_state=1)
    df_over_9 = df[df['Daily_Screen_Time'] >= 9].dropna().sample(150, random_state=2)

    # Combine and copy
    df_clean = pd.concat([df_under_9, df_over_9]).copy()

    # Exaggerate Happiness Index values
    df_clean['Happiness_Index'] = df_clean['Daily_Screen_Time'].apply(
        lambda x: np.random.uniform(0, 2) if x < 9 else np.random.uniform(18, 25)
    )

    # Add jitter to both x and y
    df_clean['Jittered_Screen_Time'] = df_clean['Daily_Screen_Time'] + np.random.normal(0, 0.3, len(df_clean))
    df_clean['Jittered_Happiness'] = df_clean['Happiness_Index'] + np.random.normal(0, 0.5, len(df_clean))

    # Steep curve using higher-degree polynomial
    coeffs = np.polyfit(df_clean['Jittered_Screen_Time'], df_clean['Jittered_Happiness'], 4)
    trendline = np.poly1d(coeffs)
    x_range = np.linspace(df_clean['Jittered_Screen_Time'].min(), df_clean['Jittered_Screen_Time'].max(), 200)
    y_trend = trendline(x_range)

    # Build plot
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_clean['Jittered_Screen_Time'],
            y=df_clean['Jittered_Happiness'],
            mode='markers',
            name='100% Real Human Feelings',
            marker=dict(
                color='gray',
                size=9,
                line=dict(width=1, color='DarkSlateGrey')
            ),
            opacity=0.5,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x_range,
            y=y_trend,
            mode='lines',
            name='Certified Trendline',
            line=dict(color='royalblue', width=4, dash='dash')
        )
    )

    fig.update_layout(
        title="📈 The Science is Settled: Happiness Blasts Off at 9 Hours",
        xaxis=dict(
            title="Daily Screen Time (hrs)",
            showline=True,
            showticklabels=True,
            ticks='inside',
            tickcolor='gray',
            tickfont=dict(color='gray'),
            linecolor='gray',
            zeroline=False,
        ),
        yaxis=dict(
            title="Happiness Index",
            showline=True,
            showticklabels=True,
            ticks='inside',
            tickcolor='gray',
            tickfont=dict(color='gray'),
            linecolor='gray',
            zeroline=False,
        ),
        font=dict(color='gray'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=40, r=40, t=60, b=40),
        title_font_size=22,
        showlegend=True,
        legend=dict(
            orientation='h',
            x=0.98,
            y=1.15,
            xanchor='right',
            yanchor='top',
            bgcolor='rgba(255, 255, 255, 0.7)',  # optional: semi-transparent background
            bordercolor='gray',
            borderwidth=1,
            font=dict(color='gray')
        )
    )

    return fig



def correlation_heatmap(df):
    df_renamed = df.copy()
    df_renamed = df_renamed.rename(
        columns={
            'Daily_Screen_Time': 'Screen Time (hrs)',
            'App_Social_Media_Time': 'Social Media Time (hrs)',
            'Well_Being_Score': 'Well-Being Score',
            'Mood_Rating': 'Mood Rating',
            'Inverted_Stress_Level': 'Stress Level',
        }
    )

    cols = [
        'Screen Time (hrs)',
        'Social Media Time (hrs)',
        'Well-Being Score',
        'Mood Rating',
        'Stress Level',
    ]
    corr_matrix = df_renamed[cols].corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        title="Statistically Speaking... You Need More TikTok!"
    )
    fig.update_layout(
        margin=dict(l=40, r=40, b=50, t=50),
        width=600,  # Set a fixed width
        height=500,  # Optional, keep it balanced
        coloraxis_colorbar=dict(
            x=1.2,  # MUCH closer to the heatmap
            thickness=15,
            title='Correlation',
            tickvals=[-1, -0.5, 0, 0.5, 1]
        )
    )
    return fig


def efficiency_index_fig(df):
    color_map = {'Elite': 'green',
                 'Average': 'yellow',
                 'Underperforming': 'red'
    }

    fig = px.bar(
        df,
        x='Participant_ID',
        y='Screen_Joy_Efficiency_Index',
        color='Efficiency_Zone',
        color_discrete_map=color_map,
        labels={'Screen_Joy_Efficiency_Index': 'Screen Joy Efficiency Index'},
        title="Screen Joy Efficiency Index by Participant",
    )

    fig.update_layout(
        xaxis_title='Participant ID',
        yaxis_title='Screen Joy Efficiency Index',
        barmode='group',
        template='plotly_dark',
    )
    return fig

