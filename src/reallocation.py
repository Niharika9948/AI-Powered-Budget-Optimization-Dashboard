def suggest_reallocation(df):
    """Suggest departments with under-utilized budget for reallocation"""
    under_utilized = df[df['predicted_utilization'] < 0.8]
    suggestions = under_utilized[['department', 'budget', 'predicted_expenditure']]
    print("Suggested reallocation:")
    print(suggestions)
    return suggestions