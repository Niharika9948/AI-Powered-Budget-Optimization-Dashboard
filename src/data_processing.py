import pandas as pd

def load_budget_data(file_path):
    """Load budget vs expenditure CSV"""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess data and calculate utilization"""
    df.fillna(0, inplace=True)
    df['utilization'] = df['expenditure'] / df['budget']
    return df