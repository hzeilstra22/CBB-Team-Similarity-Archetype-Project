import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def draw_radar_plot(table,metrics,stat_dict):
    '''
    args:
    table: DataFrame containing the statistics to plot
    metrics: List of metrics to include in the radar plot

    returns:
    None, draws a radar plot
    '''
    df=table[0:3].set_index('Team').transpose()
    colors=table[0:3].set_index('Team').loc[df.columns,'hexColor1']
    colors2=table[0:3].set_index('Team').loc[df.columns,'hexColor2']
    colors=colors.drop_duplicates()
    colors2=colors2.drop_duplicates()
    df=df.loc[metrics]

    df.index=df.index.map(stat_dict)
    fig=go.Figure()

    for team in df.columns:
        fig.add_trace(go.Scatterpolar(
         r=df[team],
            theta=df.index,
            fill='toself',
            fillcolor=colors.loc[team],
            opacity=0.5,
            name=team,
            line=dict(color=colors2.loc[team],width=2)
    ))

    fig.update_traces(hovertemplate='Percentile: %{r:.2f}<br>Stat: %{theta}')


    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,1]
            )
        ), showlegend=True, 
        title='Duke Shooting Comparison',
        title_x=0.5
    )

    fig.show()
