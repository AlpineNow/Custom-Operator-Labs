Minimum Alpine Version: 6.3

An operator which filters for rows containing null values and writes them to a file.

Badly typed values (such as a double in a string column) will not appear at all, because Spark excludes them when loading a DataFrame.