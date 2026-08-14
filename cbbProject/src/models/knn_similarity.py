from sklearn.neighbors import NearestNeighbors
import pandas as pd

def generate_comps_table(team, season, metrics,rank, stats_scaled,same_season=False):
    '''
    args: 
    team: The team for which to generate the comparison table
    season: The season for which to generate the comparison table
    metrics: The metrics to include in the comparison table
    same_season: Whether to only include teams from the same season

    returns: 
    DataFrame containing the comparison table
    '''
    X=stats_scaled[metrics].astype(float).to_numpy()

    knn=NearestNeighbors(n_neighbors=100,metric='cosine')

    knn.fit(X)  
    team_index=rank[(rank.teamMarket==team)&(rank.competitionId==season)].index[0]
    distances,indices=knn.kneighbors(X[team_index].reshape(1,-1))
    indices=indices[0]
    table=rank.iloc[indices][['teamId','competitionId','teamMarket','competitionName']]

    table['similarity']=1-distances[0]

    table=pd.merge(table,rank,on=['teamId','competitionId','teamMarket','competitionName'],how='left')

    if same_season:
        table=table[table['competitionId']==season][0:11]
    else:
        table=table[0:11]

    table['Team']=table['teamMarket'] + ' ' + table['competitionName'].astype(str).str[:7]

    columns_to_include=['Team','similarity','hexColor1','hexColor2']+metrics

    table=table[columns_to_include]

    return table