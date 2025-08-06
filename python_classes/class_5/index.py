# Function to greet everyone
def greet():
    print("Hello EveryOne")
    print("Hello Uziar")
    print("Hello Maten")
    print("Hello Uziar")

# Calling the greet function to run the code inside it
greet()


# Simple variable assignment
num5 = 56
print("num5", num5)


# Function with parameters and default values
# num2 and num3 have default values (5 and 30)
def sum(num1, num2=5, num3=30):
    res = num1 + num2 + num3  
    return res             


# This line will give error because "res" is not defined yet
print("res", res)

# Correct usage after calling the function
num4 = 50

# Calling the sum function with 2 arguments (num1=50, num2=30)
# num3 will take the default value 30
res = sum(num4, 30)
print('res: ', res)


# List of numbers
list_data = [10, 220, 40, 50]

# Function to print each item in the list
def print_list(list):
    for item in list:               
        print("item", item)

# Call the function to print list items
print_list(list_data)


# Another function to calculate the sum using sum() function
def cal():
    sumRes = sum(20, 30, 40)  
    print("sumRes", sumRes)

# Call the cal function
cal()
