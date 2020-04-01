from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import roc_auc_score

def NonLinear_Model(X_train, Y_train, X_test, Y_test):
    ## Proceed To Prepare Linear SVM
    linear_svc = SVC(kernel='rbf')
    linear_svc.fit(X_train, Y_train)

    ## Proceed to Test Performance on the Training Dataset
    Y_train_predict = linear_svc.predict(X_train)

    ## Proceed to write accuracy
    train_accuracy = accuracy_score(Y_train,Y_train_predict)
    train_precision = precision_score(Y_train, Y_train_predict)
    train_recall = recall_score(Y_train, Y_train_predict)
    train_auc = roc_auc_score(Y_train, Y_train_predict)

    print("Training Results")
    print("Accuracy on Training:", round(train_accuracy,3))
    print("Precision on Training:", round(train_precision, 3))
    print("Recall on Training:", round(train_recall,3))
    print("AUC on Training:", round(train_auc,3))

    ## Proceed to Test on Testing Dataset
    Y_test_predict = linear_svc.predict(X_test)

    # Proceed to Calculate Scores
    test_accuracy = accuracy_score(Y_test,Y_test_predict)
    test_precision = precision_score(Y_test, Y_test_predict)
    test_recall = recall_score(Y_test, Y_test_predict)
    test_auc = roc_auc_score(Y_test, Y_test_predict)

    print("\nTesting Results")
    print("Accuracy on Testing:", round(test_accuracy,3))
    print("Precision on Testing:", round(test_precision, 3))
    print("Recall on Testing:", round(test_recall,3))
    print("AUC on Testing:", round(test_auc,3))

    ## Proceed to Graph ROC Curve
    plot_roc_curve(linear_svc, X_test, Y_test)