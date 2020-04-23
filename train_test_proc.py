def deps_and_indeps(my_df, my_x_list, my_y_list, id_field, test_perc):
    """
    Split dataset into indep and dep variables
    """
    # Independent Variables
    x_df = my_df[my_x_list]  # Features
    
    # Dependent Variables
    y_df = my_df[my_y_list]
    X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=test_perc)
    return X_train, X_test, y_train, y_test
