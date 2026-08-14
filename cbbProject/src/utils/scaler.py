from sklearn.preprocessing import StandardScaler
def scale_features(group,columns):
    '''Scales the specified columns of the input data frame using standard scaler'''
    scaler=StandardScaler()
    group[columns]=scaler.fit_transform(group[columns])
    return group