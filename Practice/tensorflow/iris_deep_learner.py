from sklearn import metrics
import sklearn.model_selection as cross_validation
import tensorflow as tf
from tensorflow.contrib import learn

if __name__ == '__main__':
    iris = learn.datasets.load_dataset('iris')
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.2,
                                                                         random_state=42)
    classifier = learn.DNNClassifier(
        feature_columns=[tf.contrib.layers.real_valued_column("", dimension=x_train.shape[1])],
        hidden_units=[10, 20, 10], n_classes=3)
    classifier.fit(x_train, y_train, steps=200)
    pred = classifier.predict(x_test)
    pred = (list(pred))
    score = metrics.accuracy_score(y_test, pred)
    print('Accuracy', score)
