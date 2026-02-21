def compare_budget(df):
    """Identify under-utilized departments (<80% utilization)"""
    under_utilized = df[df['utilization'] < 0.8]
    print("Departments with under-utilized budget:")
    print(under_utilized)
    return under_utilized