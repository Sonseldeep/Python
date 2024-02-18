# Find Standard Deviation
# Easy
# Program Description
# Write a program to find standard deviation using the stdev() function of the statistics module.

# Import the statistics module.
# Create a list of data 2, 4, 6, 8, 10 and assign it to data_set variable.
# Print the standard deviation of data_set using stdev().


# import statistics module
import statistics as st

# create a data_set variable
data_set = [2,4,6,8,10]

# use stdev() to find the standard deviation of data_set
print(st.stdev(data_set))