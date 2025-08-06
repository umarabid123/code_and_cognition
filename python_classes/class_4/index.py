# Print table of any number using while loop

num = 2       
i = 1         # Starting from 1
end = 10      # Ending at 10

while i <= end:  # Loop will run from 1 to 10
    print(f"{num} * {i} = {num * i}")   # Print the multiplication result
    i += 1     # Increase i by 1 after each loop


# Print table of any number using for loop

num = 2
end = 10

for i in range(1, end + 1):     # Loop from 1 to 10
    print(f"{num} * {i} = {num * i}")   # Example: 2 * 1 = 2



# Print a number using normal print
number = 10

print("the number is: ", number)         # Old method
print(f"the number is: {number}")        # f-string (modern way)



# Find a number in a list

# A list is a data structure that stores multiple values
arr = [1, 2, 3, 4, 5]   # List of numbers
target = 4              # We want to find the position of 4

# Loop through the list using index
for i in range(len(arr)):   # len(arr) gives the size of the list
    if arr[i] == target:    # Check if current item equals the target
        print(i)            # Print the index (position) of the target
