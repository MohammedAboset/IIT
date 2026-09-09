# Week 5 Exercises

# Ex1
num = 5
while True:
    num = 2 * num
    if num % 4 == 0:
        break
print(num) #20

# Ex2
num = 3
while num < 15: # 3 < 15 True, 8 < 15 True, 13 < 15 True, 18 < 15 False 
    num += 5
print(num) # 18

# Ex3
oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1 # i=4
while i >= 0: # 4>-0 True, 3 >=0 True, 2 >=0 True, 1>=0 True, 0>=0 True, -1 >=0 False 
    if len(oceans[i]) < 7: # 9 < 7 False, 6 < 7 True, 6 < 7 True, 7 < 7 False, 8 < 7 False
        del oceans[i] # del Arctic, del Indian, 
    i = i - 1 # i = 3, i = 2, i = 1, i = 0, i = -1
print(", ".join(oceans)) # Atlantic, Pacific, Antartic

# Ex4
for i in range(3, 7): # i=3, i=4, i=5, i=6, i=7: does not show because 7 is not less than 7
    print(2 * i) # 6/n, 8/n, 10/n, 12
    
# Ex5 
num = 5
for i in range(num, 2 * num - 2): # range(5, 8) 
    print(i) #5/n, 6/n, 7/n

# Ex6
for countdown in range(10, 0, -1): # start=10, end=0, step=-1
    print(countdown)

# Ex7
numEvens = 0
sumOfEvens = 0

list1 = [2, 9, 6, 7, 12]
for num in list1:
    if num % 2 == 0: # 2%2=0 T, F, 6%2=0True, F, T
        numEvens += 1 # numEvens =1, numEvens = 2, 3
        sumOfEvens += num # sumEvens = 2, sumEvens = 8, 20 
print(numEvens, sumOfEvens) # 3, 20 

# Ex8
numOfNumbers = 0
list1 = ["three", 4, 5.7, "six", "seven", 8, 3.1416]
for item in list1:
    if isinstance(item, str): # T, F, F,
        continue 
    numOfNumbers += 1 # numOFNumbers = 1, 2, 3, 4
print(numOfNumbers) # 4

# Rewrite using a for loop

#Ex9
# num = 1
# while num <= 9:
   # print(num)
   # num += 2
for num in range(1, 10, 2):
    print(num)

# Ex10
# total = int(input("Enter a number: "))
# num = int(input("Enter a number: "))
# total = total + num
# num = int(input("Enter a number: "))
# total = total + num
# print(total)

total = int(input("Enter a number: "))
counter = 1
while counter <= 2:
    num = int(input("Enter a number: "))
    total = total + num
    counter += 1 
print(total)

# Determine the output displayed

# Ex11
L = ["sentence", "contains", "five", "words."]
L.insert(0, "This")
print(" ".join(L))

del L[3]
L.insert(3, "six")
L.insert(4, "different")
print(" ".join(L))
# This sentence contains five words.
# This sentence contains six different words.

# Ex12
# Assume the name entered is: Damith Hearth
name = input("Enter name with two parts: ")
L = name.split()
print("{0:s}, {1:s}".format(L[1], L[0]))
# Enter name with two parts: Mohammed Aboset
# Aboset, Mohammed

# Ex13
nums = [6, 2, 8, 1]
print("Largest Number:", max(nums))
print("Length:", len(nums))
print("Total:", sum(nums))
# Largest Number: 8
# Length: 4
# total: 17

# Ex14
tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print(" ".join(tuple2))
# When in the course of human events

# Identify all errors

# Ex15
# Four virtues presented by Plato
virtues = ("wisdom", "courage", "temperance", "justice")
print(virtues[3]) # The error is the number 4 because python starts counting from 0 so it should be 3 

# Ex16
list1 = ["1", "two", "three", "4"] # join() only works with strings and 1, 4 are integers so add quotation marks to change them into a string
print(" ".join(list1))

# Ex17
## Display the numbers from 1 through 5.
num = 0 # num = 1 is inside the loop so it keeps resetting num to 1. This creates an infinite loop printing 1
while num <= 5: # First error is missing colon after while 
    print(num)
    num += 1



