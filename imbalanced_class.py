from sklearn.utils import resample


def upsample(my_df, my_y):
    """
    Function to upsample using resample without creating new dfs
    """
    df_maj = my_df[my_df['Monetary.Relief']==False]
    df_min_up = resample(my_df[my_df['Monetary.Relief']==True]
                         ,replace=True
                         ,n_samples=count_norelief
                         ,random_state=123
                        )
    return pd.concat([df_maj, df_min_up])


def downsample(my_df, my_y):
    df_min = my_df[my_df['Monetary.Relief']==True]
    df_maj_up = resample(my_df[my_df['Monetary.Relief']==False]
                         ,replace=True
                         ,n_samples=count_relief
                         ,random_state=123
                        )
    return pd.concat([df_maj_up, df_min])   
