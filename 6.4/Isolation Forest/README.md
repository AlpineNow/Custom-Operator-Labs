This is a Spark implementation of the Isolation Forest algorithm[1] for unsupervised outlier detection. The algorithm works well on high-dimensional datasets with large numbers of data points. 

The operator takes an input dataset, a set of predictor columns, an index/label column, the number of trees to use in the training procedure, and the "contamination" (i.e. the assumed concentration of outliers in the dataset). The operator then determines the outliers using the Isolation Forest algorithm and generates an output dataset that is a list of the corresponding labels/indices for the outliers.

The provided dataset is a list of FFT-transformed flattened time series data that describe the evolution of entries/exits into a building on a daily basis (a modified version of the UCI ML People Counts dataset [2]). The FFT-transformed dataset is used to demonstrate that the Isolation Forest algorithm does a good job determining which dates had abbormal flows of people due to events such as a conference in the building.

[1] https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf
[2] http://archive.ics.uci.edu/ml/datasets/CalIt2+Building+People+Counts
