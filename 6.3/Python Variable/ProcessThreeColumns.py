import sys
import csv

# This demonstrates how we can you use multiple input columns in our python script. The following script
# takes three input columns, one string column and two numeric columns. The columns MUST appear in the
#dataset in the order that the script will process them, although they do not need to be adjacent.
#This script creates a new column that is a string with the value of the string column concatenated
#with the product of the two numeric columns.
#For example if the values of the three columns in one row of the input dataset were (in order)
# "thing", "3", "2"
# the value of that new column for that row would be:
# "thing:6"


try:
    for x in sys.stdin:
        try:
            #we use python's built in CSV parsers with comma as the delimiter
            inputRow = list(csv.reader([x], delimiter = ','))[0] #input row will be a list of values
            firstCol = inputRow[0]  # a string
            secondCol = float(inputRow[1]) #numeric
            thirdCol = float(inputRow[2]) #numeric
            product = secondCol + thirdCol
            outputCol = firstCol + ":" + str(product)
            sys.stdout.write(str(outputCol) + "\n")
        except Exception:
            sys.stdout.write("exception writing line " + x)
except Exception:
    #If there is an error write a blank line so that the file lines will match up
    sys.stdout.write("\n")