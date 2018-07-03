Spark ML - Generalized Linear Regression Models

This is an implementation of the Generalized linear models that leverages the off-the shelf implementation of Generalized linear regression in Spark ML (See https://spark.apache.org/docs/latest/ml-classification-regression.html#generalized-linear-regression) and (https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.ml.regression.GeneralizedLinearRegression). 

The operator can be used to fit a regression model to predict a dependent variable that follows some distribution from the exponential family of distributions. We leverage the Mllib implementation of generalized linear regression, hence expect the user to have spark version 2.0 or greater available. 

An example of this operator is provided in Spark_ML_GLM.afm. The workflow requires connecting the crabs dataset (also in this repository). In the example we predict the “SATELLTS” column.
