Minimum Alpine Version: 6.2

The *Neural Networks* operator is Spark Modeling operator which trains a Neural Network Classification Model from MLLib MultiLayerPerceptronClassifier (feed forward back propagation).
Training parameters are: layers, max iterations, tolerance, seed, blocksize. Optimizer is L-BGFS (quasi-Newton method), which tends to converge
faster than SGD (stochastic gradient descent). Adaptive step size and regularization is included in L-BGFS optimizer.

You can find more details at:
- https://spark.apache.org/docs/1.6.1/ml-classification-regression.html#multilayer-perceptron-classifier
- http://spark.apache.org/docs/latest/mllib-optimization.html

It supports multi-class dependent variable, and categorical independent features by using One Hot Encoding before training the model.
- We throw an error if categorical columns have only 1 distinct value, or too many categories. Same for dependent column.
- We recreate the NN topology and return a wrapper of  PipelineClassificationModel (including one hot encoding) so that the trained model can be used with Alpine classification model evaluators like Confusion Matrix, Classifier..etc
