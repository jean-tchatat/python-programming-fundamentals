# Exercise07.py
# Name: Jean Tchatat
# Exercise07 While Loops
# SCAN: Start, Continue, Actions, Next iteration

#1.
number = int(input("#1. Enter a number (0 to quit): "))  # Start
while number != 0:  # Continue
    # Actions
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    number = int(input("Enter a number (0 to quit): "))  # Next iteration

#2.
count = 0  # Start
while count < 10:  # Continue
    print("+")  # Actions
    count += 1  # Next iteration

#3. 
number = 10  # Start
while number > 1:  # Continue
    print("~")  # Actions
    number -= 1  # Next iteration

#4.
name = input("#4. Enter a name (q to quit): ")  # Start
while name != "q":  # Continue
    print(f"Hello {name}")  # Actions
    name = input("Enter a name (q to quit): ")  # Next iteration

#5.
pet_name = input("#5. Enter a pet name (q to quit): ")  # Start
while pet_name != "q":  # Continue
    print(f"Pet name: {pet_name}")  # Actions
    pet_name = input("Enter a pet name (q to quit): ")  # Next iteration

#6.
# Start
total_score = 0
score_count = 0
score = float(input("#6. Enter a score (-1 to quit): "))
while score != -1:  # Continue
    # Actions
    total_score += score
    score_count += 1
    score = float(input("Enter a score (-1 to quit): "))  # Next iteration

if score_count > 0:
    average_score = total_score / score_count
    print(f"Average score: {average_score:.2f}")
else:
    print("No scores entered.")

#7.
# Start
total_weight = 0
weight = float(input("#7. Enter a weight (-1 to quit): "))
while weight != -1:  # Continue
    total_weight += weight  # Actions
    weight = float(input("Enter a weight (-1 to quit): "))  # Next iteration
print(f"Total weight: {total_weight:.2f}")

#8. Trace the loop.
# Iteration 1: i = 1, print +, then i = 5.
# Iteration 2: i = 5, print +, then i = 9.
# Iteration 3: i = 9, print +, then i = 13.
# Iteration 4: i = 13, print +, then i = 17.
# Stop because 17 < 15 is false.
# Answer: 4 plus signs are printed. Final value of i is 17.
i = 1  # Start
while i < 15:  # Continue
    print("+")  # Actions
    i += 4  # Next iteration
print("i=", i)
