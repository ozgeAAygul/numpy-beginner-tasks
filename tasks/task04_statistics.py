import numpy as np

# 1D Array
scores = np.array([70, 85, 90, 60, 75])
# Calculate the average
average = np.mean(scores)
print(f"{average:.2f}")
# Calculate the median
median = np.median(scores)
print(median)
# Calculate the standard deviation
s_dev = np.std(scores)
print(f"{s_dev:.2f}")
# Calculate the min value
min_val = np.min(scores)
print(min_val)
# Calculate the max val
max_val = np.max(scores)
print(max_val)
# Calculate the sum of all values
total_score = np.sum(scores)
print(total_score)

# 2D Array
grades = np.array([[70, 80, 90], [60, 75, 85], [90, 95, 100]])
# Average of the entire array
grades_average = np.mean(grades)
print(f"{grades_average:.2f}")
# Row-based average
grades_average_row = np.mean(grades, axis=1) # axis=1: row-wise operations (rows are aggregated)
print(np.round(grades_average_row, 2)) #:.2f eror veriyor birden fazla değer döndürdüğü için
# Column-based average
grades_average_column = np.mean(grades, axis=0) #axis=0: column-wise operations (columns are aggregated)
print(np.round(grades_average_column, 2))
# Row-based total
grades_sum_row = np.sum(grades, axis=1)
print(grades_sum_row)
# Column-based maximum value
grades_max_column = np.max(grades, axis=0)
print(grades_max_column)