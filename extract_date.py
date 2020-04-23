def extract_date(df,column):
    """
    function for extracting year and month to create new columns in a dataframe
    
    df = input dataframe
    column = columns takes a string for column name
    """
    df[column+"_year"] = df[column].apply(lambda x: x.year)
    df[column+"_month"] = df[column].apply(lambda x: x.month)
