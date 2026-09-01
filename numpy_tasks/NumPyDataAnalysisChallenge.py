import string

import numpy as np

## Numbers 1–50 ##
arr= np.arange(1,51)
print(arr)

## Even numbers 2–100 ##
even = np.arange(2, 101, 2)
print("Even:", even)

## Odd numbers 1–99 ##
odd =  np.arange(1,100,2)
print("Odd:", odd)

## Student Marks Analysis ##
marks = np.array([
78, 85, 92, 67, 88,
73, 95, 60, 84, 91
])


## Total marks ## 
print(f"Total marks: {marks.sum()}")
## Average ##
print(f"Average marks: {marks.mean()}")
## Maximum ##
print(f"Maximum marks: {marks.max()}")
## Minimum ##
print(f"Minimum marks:{marks.min()}") 
## Median ##
print(f"Median marks: {np.median(marks)}")

##Filtering
##From the marks array, find students scoring
#Above 90
print("## Above 90 ##")
print(marks[marks>90])
#Above average
print("## Above average ##")
print(marks[marks>marks.mean()])
#Below 70
print("## Below 70 ##")
print(marks[marks<70])

##Reshaping
##Create numbers 1–20 and reshape them into
## 4 × 5

test_input=  np.arange(1,21)
print("input array:",test_input)
print("4 * 5 reshape",test_input.reshape(4,5))

## Two-Dimensional Array ##
print("## Two-Dimensional Array ##")
two_d_array=np.array([[10,20,30],
                      [40,50,60]])
print(two_d_array)

## Create a 3×3 matrix and demonstrate ##
print(" 3×3 matrix ")
matrix = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
        ])
print("Matrix:")
print(matrix)

## Row selection ##
print("row 1",matrix[0])
print("row 2",matrix[1])
print("row 3",matrix[2])
## Column selection ##
print("col 1",matrix[:,0])
print("col 2",matrix[:,1])
print("col 3",matrix[:,2])
## Individual element selection ##
print("Individual element",matrix[0, 0])  
print("Individual element",matrix[1, 1])  
print("Individual element",matrix[2, 2]) 



a = np.array([10, 20, 30, 40, 50])

b = np.array([5, 10, 15, 20, 25])

## perform
## Addition
print("Addition", a+b)
## Subtraction
print("Subtraction", a-b)
## Multiplication
print("Multiplication", a*b)
## Division
print("Multiplication", a/b)


##Statistical Analysis
##Generate 100 random numbers and calculate
##Mean
##Median
##Standard deviation
##Variance

random_numbers = np.random.randint(1,1000,100)

print("Mean",np.mean(random_numbers))
print("Median",np.median(random_numbers))
print("Standard deviation",np.std(random_numbers))
print("Variance",np.var(random_numbers))

# Sorting
# Create an unsorted NumPy array and display ascending and descending results.

chars = list(string.ascii_uppercase)
arr = np.array([
    ''.join(np.random.choice(chars, 8))
    for _ in range(50)
    ])
#print(arr)
print("ascending")
print(np.sort(arr))
print("descending")
print(np.sort(arr)[::-1])

# Unique Values
# Given
input_array= [1,2,2,3,3,3,4,5,5,6]

# find unique values.
print("unique values", np.unique(input_array))

# Matrix Operations
# Create two 3×3 matrices and perform
array1= np.random.randint(1,100,(3,3))
array2= np.random.randint(2,200,(3,3))
print("array1",array1)
print("array2",array2)
# Addition
print("Addition",array1+array2)
# Subtraction
print("Subtraction",array1-array2)
# Element-wise multiplication
# Matrix multiplication
print("multiplication",array1*array2)


salaries = np.array([
        35000, 42000, 50000,
        38000, 60000, 45000,
        55000, 48000, 70000,
        52000, 39000, 65000,
        47000, 58000, 75000
        ])
print(salaries)

# Highest salary
print("Highest salary",salaries.max())
# Lowest salary
print("Lowest salary",salaries.min())
# Average salary
print("Average salary",salaries.mean())
# Employees earning above average
print("Employees earning above average",salaries[salaries>salaries.mean()])


# Generate a 5×5 random integer matrix and determine
random_55=  np.random.randint(1,100,(5,5))
print("5 x 5 matrix",random_55)
# Maximum value
print("Maximum value",random_55.max())
print("Maximum value",random_55.max(axis=1))
# Minimum value
print("Minimum value",random_55.min())
print("Maximum value",random_55.max(axis=0))
# Row-wise sum
print("Row-wise sum",random_55.sum(axis=1))
# Column-wise sum
print("Column-wise sum",random_55.sum(axis=1))
# Overall average
print("Overall average",random_55.mean())
