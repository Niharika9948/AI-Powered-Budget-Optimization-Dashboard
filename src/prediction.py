from sklearn.linear_model import LinearRegression

def predict_utilization(df):
    """Predict next period utilization using simple linear regression"""
    # Simple assumption: next period budget same as current
    model = LinearRegression()
    model.fit(df[['budget']], df['expenditure'])  # train on 'budget'
    
    # Predict using the same column name
    df['predicted_expenditure'] = model.predict(df[['budget']])
    df['predicted_utilization'] = df['predicted_expenditure'] / df['budget']
    
    return df