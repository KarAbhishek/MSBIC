# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier


# def init_decision_tree():
#     DecisionTreeClassifier(labelCol=label, featureCol=)
#
#
# def random_forest():
#     RandomForestClassifier(labelCol=label, featuresCol="features", maxBins=maxbins)


# # Loading Data into the Data Frame
# # Set up a Pipeline Definition
# # Define Model / Estimation Definition
# # Transformation Definition
# # Evaluation strategy - Cross validation/ Train-Test split
# # Performance Output
# # Any parameter grid exploration desired

# paramGrid = ParamGridBuilder().addGrid(hashingTF.numFeatures, [10, 100, 1000]).addGrid(lr.regParam, [0.1, 0.01]).build()
# crossval = CrossValidator(estimator=pipeline, estimatorParamMaps=paramGrid, evaluator=BinaryClassificationEvaluator(),
#                           numFolds=2)  # Use 3+ folds in practice
# cvModel = crossval.fit(training)
