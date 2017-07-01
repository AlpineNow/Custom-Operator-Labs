Minimum Alpine Version: 6.3

The *Binary Classifier* operator is Spark Prediction operator for binary or multi-class classification.
It enables the user to make new binary predictions based on a confidence threshold associated with a class specified by the user (compared to classic prediction of the class with highest confidence).
The optimal confidence threshold can be determined using the Classification Threshold Tuning operator.

For a multi-class classification, the user needs to specify the prediction string to use for all other classes (different from 'Class to Predict').
For a binary classification, we take the other class by default.

