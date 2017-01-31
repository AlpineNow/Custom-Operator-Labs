The *Sessionization* operator is Spark Transformation operator that identifies sessions in time series-data (widely used in web analytics, predictive maintenance etc...)

From an HDFS input with a timestamp column (and optional user ID column(s) and status column), it creates 2 additional columns "new_session" (1 or 0) and "session_id" for each user (if id columns are specified) or the whole input.
A new session can be defined in 2 ways:
- Change of status: when the value of the status column is different from the previous value (sorted by time per user)
- Time Interval Threshold: when the time difference between 2 rows (sorted by time per user) is above a specified threshold (e.g: 10 s)

