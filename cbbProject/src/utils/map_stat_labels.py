import pandas as pd
def map_stat_labels(table):
    '''
    args:
    table: DataFrame containing the statistics to map

    returns:
    DataFrame with mapped column labels
    '''

    stat_dict=pd.read_csv('/Users/hannahzeilstra/Downloads/cbbProject/data/data_dictionary.csv')
    stat_dict=dict(zip(stat_dict['key'],stat_dict['label2']))
    stat_dict['tovPctAgst']='Opponent TOV%'
    stat_dict['lane2FgPctAgst']='Opponent LANE2 FG%'
    stat_dict['lane2FgaFreqAgst']='Opponent LANE2 FGA%'
    stat_dict['fga3RateAgst']='Opponent 3PAr'
    stat_dict['fg3PctAgst']='Opponent 3P%'
    
    table.columns=table.columns.map(lambda x: stat_dict.get(x,x))
    return table