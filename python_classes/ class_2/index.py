# Example 1: IF-ELIF-ELSE
a = 10
b = 10

# Check if a is greater than b
if a > b:  # This is FALSE because 10 is not greater than 10
    print("a is greater than b")  # This will not run

# Check if a is equal to b
elif a == b:  # This is TRUE because 10 == 10
    print("a is equal to b")  # ✅ This will run

# If both conditions are false, run else
else:
    print("b is greater than a")  # This will not run



# Example 2: NOT operator
a = 5
b = 12

# not a > b means "if a is NOT greater than b"
# a > b → 5 > 12 → FALSE, so not FALSE → TRUE
if not a > b:  
    print("a is not greater than b")  # ✅ This will run

else:
    print("above condition false")



# Example 3: AND operator
a = 10
b = 15
c = 20

# a < b → 10 < 15 → TRUE
# c < a → 20 < 10 → FALSE
# TRUE and FALSE → FALSE
if a < b and c < a:  
    print("both conditions are true")

else:
    print("condition false")  # ✅ This will run



# Example 4: OR operator
a = 10
b = 15
c = 20

# a > b → 10 > 15 → FALSE
# b > c → 15 > 20 → FALSE
# FALSE or FALSE → FALSE
if a > b or b > c:  
    print("at least one condition is true")

else:
    print("both conditions are false")  # ✅ This will run
