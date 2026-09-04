# 12.1) Write a line of Python code that displays the sum of 468 + 751.
print(468+751)

# 12.2) Write a line of Python code that displays the words "How are you?" to the screen.
print("How are you?")

# 12.3) What is the output of the following Python statement?
# print(8 / 3, 4 * 7, 9 + 13, 2 ** 5, 6 * (3 + 2))
print(8 / 3, 4 * 7, 9 + 13, 2 ** 5, 6 * (3 + 2))

# 12.4) Write a Python statement that creates a variable called size and assigns the value 77 to it.
siz = 77

# 12.5) What will be the output of the following Python program?
x = 5
y = 7
print(abs(x - y) - 10)
print(int(x ** 2) + 1.4)
print(round(y + 3.14159, 2))

# 12.6) What is the output of the following Python program?
a = 31
b = 7
print(a // b, a % b)

# 12.7) Write a Python program to convert 250 minutes into hours and minutes and print both values.
minutes = 250

hours = minutes // 60
remaining_minutes = minutes % 60

print(hours)
print(remaining_minutes)

# 12.8) What is the output of the following Python program?
str1 = "it is what it is"
print(str1.find("is"), str1.rfind("it"), str1[-9:-7])

# 12.9) What is the output of the following Python program?
str1 = "it is what it is"
print(str1[-9:])

# 13-16) Assume a = 1 and b = 1.5. For each condition, state whether it evaluates to True or False.

# 13) 3 * a == 2 * b, True
a = 1
b = 1.5
print(3 * a == 2 * b)

# 14) (a < b) or (b < a), True
print((a < b) or (b < a))

# 15) not (a < b) or not (a < (b - a)), True
print(not (a < b) or not (a < (b - a)))

# 16) ((a == b) or not (b < a)) and ((a < b) or (b == a + 1)), True 
print(((a == b) or not (b < a)) and ((a < b) or (b == a + 1)))

# 17-26) Determine whether each condition is True or False.

# 17) 'Ab' == 'ab', Python is case sensetive so A and a are different therefore cannot be equal therefore the answer is False.
print('Ab' == 'ab')

# 18) 'Harry' < 'harry', Python compares strings based on charecter values. Uppercase letter come before lower case, therefore this will be True.
print('Harry' < 'harry')

# 19) not (('B' == 'b') or ("Big" < "big")), Because one of the expressions is true and there is an or then the entire expression is true, and with the not the whole expression is reversed therefore the answer is False.
print(not (('B' == 'b') or ("Big" < "big")))

# 20) isinstance(32, float), 32 is an integer (int) not a float therefore the answer is False.
print(isinstance(32, float))

# 21) isinstance(32, int), 32 is an integer therefore this is True.
print(isinstance(32, int))

# 22) "yt" in "Python", Python has the letters yt together therefore this is True.
print("yt" in "Python")

# 23) "knight".startswith('n'), knight starts with k not n therefore this is False.
print("knight".startswith('n'))

# 24) True or False, when there is an or if one of the conditions is true the whole condition is true, therefore this is True.
print(True or False)

# 25) True and False, with and both conditions need to be true otherwise it's False.
print(True and False)

# 26) not True, not reverses the boolean value therefore this is False.
print(not True)

# 27- 29) Determine the output displayed.

# 27) 2 2 7 
a = 2
b = 3
c = 7

if (a * b) < c:
    b = a
else:
    c = a + b + c

print(a, b, c)

# 28) Assume the response is B, To be, or not to be.  
letter = input("Enter A, B, or C: ")
letter = letter.upper()

if letter == "A":
    print("A, my name is Alice.")
elif letter == "B":
    print("To be, or not to be.")
elif letter == "C":
    print("Oh, say, can you see.")
else:
    print("You did not enter a valid letter.")

# 29) Depends on what is entered - vowel, constant, or non-letter. Ex, A = A is a vowel. 
isvowel = False
letter = input("Enter a letter: ")
letter = letter.upper()

if letter in "AEIOU":
    isvowel = True

if isvowel:
    print(letter, "is a vowel.")
elif not (65 <= ord(letter) <= 90):
    print("You did not enter a letter")
else:
    print(letter, "is a consonant.")

# 30) Using the flowchart provided, write a Python program that reads a person's taxable income, computes the state income tax according to the diagram, and then displays the tax. 
income = float(input("Enter taxable income: "))

if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("Tax:", tax)







