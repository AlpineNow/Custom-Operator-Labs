This is an implementation of an automated machine learning system to compute an optimal classifier model for a given binary classification problem. The implementation is in the form of two separate operators:

- AutoML Classification Trainer
- AutoML Classification Predictor

The Trainer operator takes an input dataset with user-provided predictor columns and a response column, and performs the following steps:

1. Sets up a parameter grid for Logistic Regression, Random Forest, and Gradient Boosted Decision Tree training algorithms
2. Trains models on the parameter grid using 3-fold cross-validation
3. Computes a leaderboard based on average performance metrics (currently _accuracy_) 
4. Extracts the best model and passes it on to the Predictor operator

The Predictor operator takes a test dataset and a model from an upstream AutoML Classification Trainer (the best model on the training data), and scores the test data using the model.

The example workflow walks through a demonstration of these operators using the classic Airline Delays dataset; the latter has been processed and filtered with feature engineering already performed.