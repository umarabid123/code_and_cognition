# A recursive function to find factorial of a number
# For example, factorial of 4 is: 4 * 3 * 2 * 1 = 24

def fact(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * fact(n - 1)   # Recursive call

# Call the function with input 4

res = fact(4)
print("res: ", res)

# Explanation of how recursion works step by step:
# fact(4)
# => 4 * fact(3)
# => 4 * 3 * fact(2)
# => 4 * 3 * 2 * fact(1)
# => 4 * 3 * 2 * 1 = 24



# Recursion Example: Sum of Natural Numbers

# A recursive function to find sum of numbers from n to 1
# For example, sum(3) = 3 + 2 + 1 = 6

def sum(n):
    if n == 1:              # Base case: if n is 1, return 1
        return 1
    else:
        return n + sum(n - 1)   # Recursive call

# Call the function
print(sum(20))  




# Explanation of how recursion works step by step:
# sum(20)
# => 20 + sum(19)
# => 20 + 19 + sum(18)
# => 20 + 19 + 18 + ... + 1
# => Final result: 210
