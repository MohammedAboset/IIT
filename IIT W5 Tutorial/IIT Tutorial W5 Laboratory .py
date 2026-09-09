# Laboratory

# 1
C = 10

print("Celsius\tFahrenheit")

while C <= 30:
    F = (9/5 * C) + 32
    print(C, "\t", F)
    C += 5

# 2
phrase = input("Enter a phrase: ")
counter = 0

for char in phrase:
    if char.lower() in "aeiouy":
        counter += 1

print("The phrase contains {0} vowels.".format(counter))
