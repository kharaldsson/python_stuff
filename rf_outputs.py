"""
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
"""

def rf_regressor_outputs(regressor, feat_use_list, x_tr, x_te, y_tr, y_te, y_predictions):
    """
    Print all RF Outputs
    """
    importance_raw = list(regressor.feature_importances_)
    feat_importances = [(feature, round(importance,2)) for feature, importance in zip(feat_use_list, importance_raw)]
    feat_importances = sorted(feat_importances, key=lambda x: x[1], reverse=True)
    for pair in feat_importances:
        print('Variable: {:100} Importance: {}'.format(*pair))

        
def rf_classifier_outputs(classifier, feat_use_list, x_tr, x_te, y_tr, y_te, y_predictions):
    """
    Print all RF Outputs
    """
    print("Train Accuracy :: ", accuracy_score(y_tr, classifier.predict(x_tr)))
    print("Test Accuracy  :: ", accuracy_score(y_te, y_predictions))
    print(confusion_matrix(y_te, y_predictions))
    print(classification_report(y_te, y_predictions))
    importance_raw = list(classifier.feature_importances_)
    feat_importances = [(feature, round(importance,2)) for feature, importance in zip(feat_use_list, importance_raw)]
    feat_importances = sorted(feat_importances, key=lambda x: x[1], reverse=True)
    for pair in feat_importances:
        print('Variable: {:100} Importance: {}'.format(*pair))
