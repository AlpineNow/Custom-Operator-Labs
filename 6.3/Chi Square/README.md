Minimum Alpine Version = 6.3 

This jar contains two operators that performa a Pearson's Chi Square test -- Chi Square, Independence Test and Chi Square, Goodness of Fit. 

Chi Square, Independence Test: 
The operator should be used to determine whether categorical columns are statistically independent of a categorical dependent variable column. For example, if we have a dataset of user churn, that includes the factors gender and browser type, we could use the Independence Test operator see if there is a significant statistical relationship between gender & churn, and/or between browser & churn. We leverage the Mllib implementation of Pearson's Chi Square test of independence. 
This operator also includes the option to use a Fisher's exact test . The Fisher's exact test is a similar test for statistical significance to the Chi Square test with slightly different assumptions. The Fisher's exact test is recommended when sample sizes are small, (cell sizes less than five), and can only be calculated on 2 x 2 tables.
The operator requires one tabular input dataset on hadoop that should contain at least two catagorical columns to compare.

Chi Square, Goodness of Fit: 
The operator computes a Pearson's Chi Square test for goodness of fit of a distribution.  In this case the Chi Square test is performed on two vectors of the frequency of events, the vector of observed frequencies and the vector of expected frequencies. The null hypothesis is the the frequencies in each cell (frequency of each event occurring) are equal in the observed and expected distribution. This test differs from the test of independence, since it assumes that the degrees of freedom are equal to the number of possible events minus one.  Because this test should be used to test observed outcomes against some known theoretical distribution we have designed the operator so that it accepts the observed and expected frequency data in two different datasets, since these datasets made not be the same length. (Most likely, the expected vector is already scaled, while the observed vector comes from some real data with each observation as a row). 

