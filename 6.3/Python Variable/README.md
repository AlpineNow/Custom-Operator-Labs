Minimum Alpine Version: 6.3 
The python variable operator lets the user upload a python script that creates a new column in the dataset by transforming one or more columns in the input data. The python script will be run on the data stored in each part of your distributed dataset. The script should read from standard in and write to standard out. The input the script will receive via standard in is a text representation of the rows of each part of the distributed dataset. The operator will "clean" these inputs so that each row contains only the input column you selected (each row separated by return ("\n") characters.  If you select multiple input columns, those values will appear as a comma separated list. Your script must parse those comma separated values. For each line in standard in, your script should write one line in standard out. The values written to standard out will form the values of the new column. You may pass the python script to the operator in two ways: 
1.)Upload the python script to your cluster. You may upload a file to the cluster either by clicking the upload a dataset feature in the workflow editor or by using ssh from the command line. In this case use the "Python Script from HDFS" parameter and select your Python script in the file system. The script must be uploaded to the same datasource as the input dataset. 
2)Upload the python script to the chorus workspace.  In your workspace, navigate to the "workfiles" page. Click "Upload File" and upload the python script from your computer. You may also publish a Python notebook in your workbook as a .py. In this case, use the "Python Script from Chorus" parameter to select the .py folder from your workspace. The operator does not have access to files outside of your workspace. Note that if you use a chorus file, the chorus file must be copied to your cluster so that it can be used by the Spark workers. After the operator has completed, you will notice that a .py file will have been created in the same directory as the output of your operator. 

In this directory we have provided three example python scripts that are used in the exampel AFM. 
1. AddOne.py - This is the most simple example, expects one numeric column, parses the column as an double and then adds one to it. 
2. SkipLine.py - This shows how this operator could be used as a filter. The script only outputs a line to standard out if it is less than 80. You may only used this script if you select "Keep Old Columns" --> "No".
3.ProcessMultipleColumns - The most simple example of using multiple columns as input. It expects the user to select one string column and two numeric columns as input. It outputs one string column created from the three input three columns.