# Part A

# 1) Simple Function

# Define the function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Aisha")

# Display the result
print(message) 

# 2) Parameters and return values

# Define the function
def area_of_rectangle(width, hight):
    return width * hight

# Call the function and display the result
print(area_of_rectangle(3, 5))

# 3) Default and keyword arguments

# Define the function with a default exponent of 2
def power(base, exponent=2):
    return base ** exponent

# Use the default exponent
print(power(5))

# Use a keyword argument to change the exponent
print(power(2, exponent=3))

# 4) Docstrings & scope

# Global variable
PI = 3.14159

# Function to calculate the area of a circle
def circle_area(r):
    "Compute area of a circle of radius r."
    return PI * (r ** 2)

# Call the function and display the result
print(circle_area(2))

# 5) Quick Exercises

# Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Test the function
print(fahrenheit_to_celsius(68))

# Check if a number is even
def is_even(n):
    return n % 2 == 0

# Test the function
print(is_even(6))

# Triangle area
def triangle_area(b, h=1):
    return 0.5 * b * h

# Test the function
print(triangle_area(10))


