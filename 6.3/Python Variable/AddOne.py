import sys

# This is an example script for the python variable operator. It creates a new column that is
#one greater than the input column

# The script reads from standard in (stdin) and for each value in standard in does the following:
# Converts the input into an integer and strips it from whit space
# Adds one to the input
# Prints to standard out.
# If an exception is thrown in the loop body, the script prints a blank character to standard out.


try:
    #For each line in standard in, we must print a line to standard out
    for x in sys.stdin:
        try:
            #There may be trailing spaces so its important to strip the lines from standard int
            output_value = int(x.strip()) + 1
            #We can't print, we have to specifically write to standard out.
            #Spark will use each line as a new column
            sys.stdout.write(str(output_value) + "\n")
        except Exception:
            #If there is an exception it is best that we print an empty row. This
            #will be turned into a null by the Spark parsing code, but this way the
            #join of this new column with the original columns will not fail
            sys.stdout.write("\n")
#This is needed in case there is nothing in standard in or an IO problem.
#However if this called. There may be a problem joining this column with the others
except Exception:
    sys.stdout.write("\n")