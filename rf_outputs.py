def rf_outputs(regressor, feat_use_list, x_tr, x_te, y_tr, y_te, y_predictions):
    """
    Print all RF Outputs
    """
    importance_raw = list(regressor.feature_importances_)
    feat_importances = [(feature, round(importance,2)) for feature, importance in zip(feat_use_list, importance_raw)]
    feat_importances = sorted(feat_importances, key=lambda x: x[1], reverse=True)
    for pair in feat_importances:
        print('Variable: {:100} Importance: {}'.format(*pair))
