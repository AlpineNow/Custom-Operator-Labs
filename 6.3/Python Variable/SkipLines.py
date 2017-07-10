import sys

# This demonstrates using the python variable operator as a filter. The operator parses the input
# as an integer. However,it only outputs to standard out if the result is less than 80.
# It can only work in the instance where the operator is configure with
# 'Keep Old Columns' = 'No'
#


try:
    for x in sys.stdin:
        try:
            output_value = int(x.strip())
            # Only print to standard out if input is less than 80
            if output_value < 80:
                sys.stdout.write(str(output_value) + "\n")
        except Exception:
           pass # don't do anything since we are using this as a filter
except Exception:
    pass