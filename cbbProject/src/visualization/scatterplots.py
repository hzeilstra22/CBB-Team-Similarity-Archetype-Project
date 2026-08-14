import plotly.express as px
import pandas as pd

def plot_archetypes(
    df,
    x_col='style_x',
    y_col='style_y',
    x_title='x axis',
    y_title='y axis',
    color_col='arch_name',
    hover_cols=None,
    title='Team Shooting Archetypes'
):
    '''
    args: 
    df: DataFrame containing the data to plot
    x_col: Column name for the x-axis
    y_col: Column name for the y-axis
    x_title: Title for the x-axis
    y_title: Title for the y-axis
    color_col: Column name for the color coding
    hover_cols: List of columns to display on hover
    title: Title of the plot

    returns: 
    None, draws a scatter plot
    '''

    if hover_cols is None:
        hover_cols = []

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        hover_data=hover_cols,
        title=title
    )

    fig.update_traces(
        marker=dict(size=7, opacity=0.6),
        selector=dict(mode='markers')
    )

    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title= y_title,
        legend_title_text='Archetype',
        title_x=0.5,
        template='simple_white'
    )

    # Gridlines
    fig.update_xaxes(showgrid=True, gridwidth=1)
    fig.update_yaxes(showgrid=True, gridwidth=1)

    # Quadrant lines (optional but very useful)
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.add_vline(x=0, line_dash="dash", line_color="gray")

    fig.show()