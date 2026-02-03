import numpy as np
# np.random.seed() is used to make random results reproducible.
# Using the same seed ensures that the same random numbers are generated every time.
# The value 42 is commonly used as a seed by convention.
# Any integer could be used, but using a fixed value ensures reproducibility.
np.random.seed(42)

# Random Array
# generate numbers between 0 and 1
random_array = np.random.rand(10)
print(random_array)
# generate integers between specific integers
random_integers = np.random.randint(1, 101, size=10)
print(random_integers)
# generate numbers between 0 and 1 (2D array)
random_array2 = np.random.rand(3, 3)
print(random_array2)

# Basic simulation
dice = np.random.randint(1, 7, size=1000)
# Calculate average
dice_average = np.mean(dice)
print("Average dice value:", dice_average)
# Find the most frequent dice value
counts = np.bincount(dice) 
'''
for value, count in enumerate(counts[1:], strat=1):
  print(f"Dice {value}: {count} times")
'''
print(f"Counts for each dice value:\n{counts[1:]}")
most_frequent_value = np.argmax(counts[1:]) + 1
print("Most frequent dice value:", most_frequent_value)
