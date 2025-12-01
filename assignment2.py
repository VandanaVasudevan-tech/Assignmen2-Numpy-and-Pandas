# 1. Create a numpy array containing the numbers from 1 to 10, and then reshape it to a 2x5
# matrix.
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr.reshape(2, 5))

# 2. Create a numpy array containing the numbers from 1 to 20, and then extract the
# elements between the 5th and 15th index.

arr1 = np.arange(1, 21)
print(arr1[5:16])

# 3. How to compute the mean, median, and standard deviation of a numpy array?Use the
# array you created above.

mean_value = np.mean(arr1)
median_value = np.median(arr1)
sd_value = np.std(arr1)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard deviation :", sd_value)

# 4. Write a NumPy program that creates a 2D array x of shape (3, 4) and a 1D array y of
# shape (4,). Subtract y from each row of x using broadcasting.

x = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
y = np.array([1, 2, 3, 4])
result = x - y
print(result)

# 5.Create a dataframe with the following columns: name, age, and gender. The dataframe
# should have 10 rows of data.

data = pd.DataFrame({
    'name': ['Don', 'John', 'Oliver', 'Tommy', 'Rohit', 'Vandana', 'Gopika', 'Chahini', 'Kavya', 'Anandhu'],
    'age': [23, 34, 22, 33, 31, 30, 27, 28, 22, 29],
    'gender': ['M', 'M', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'M']
})

# 1) Add a new column to the data frame created in question 1, called occupation.
# The values for this column should be Programmer, Manager, and Analyst,
# corresponding to the rows in the dataframe.

data["occupation"] = ["Programmer", "Manager", "Programmer", "Manager", "Analyst", "Programmer", "Analyst", "Analyst",
                      "Programmer", "Analyst"]

# 2) Select the rows of the dataframe where the age is greater than or equal to 30.

result = data[data["age"] >= 30]
print("Age greater than or equal to 30 :\n", result)

# 3) Convert this dataframe to a CSV file and read that CSV file, and finally display
# the contents.

data.to_csv("output.csv", index=False)
output = pd.read_csv("output.csv")
print("Data from the csv file\n")
print(output)






