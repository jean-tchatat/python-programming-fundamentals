# Filename: select_lab01.py
# Name: Jean Tchatat
# COSC 175 HWK05

# 1
temperature = 75
humidity = 65
if temperature <= 75 or humidity < 70:
    print(f"#1. temperature={temperature}, humidity={humidity}%\n")

# 2
temperature = 105
if temperature > 100 or temperature < 0:
    print(f"#2. temperature={temperature}")
temperature = -5
if temperature > 100 or temperature < 0:
    print(f"#2. temperature={temperature}\n")

# 3
angle = 90
if angle == 90:
    print(f"#3. The angle {angle} is a right angle\n")
else:
    print(f"#3. The angle {angle} is not a right angle\n")

# 4
temp = 110
if temp >= 100:
    print(f"#4. {temp} is above the boiling point of water\n")
else:
    print(f"#4. {temp} is below the boiling point of water\n")

# 5
number = 8
posSum = 0
negSum = 0
if number >= 0:
    posSum = posSum + number
    print(f"#5. number={number}, posSum={posSum}, negSum={negSum}\n")
else:
    negSum = negSum + number
    print(f"#5. number={number}, posSum={posSum}, negSum={negSum}\n")

# 6
slope = 0.3
if slope < 0.5:
    flag = 0
    print(f"#6. slope={slope}, flag={flag}\n")
else:
    flag = 1
    print(f"#6. slope={slope}, flag={flag}\n")

# 7
mystr = "computer"
first_character = mystr[2]
second_character = mystr[4]
if second_character < first_character:
    charsum = first_character + second_character
    print(f"#7. string={mystr}, third={first_character}, fifth={second_character}")
    print(f"charsum={charsum}\n")
else:
    chardiff = ord(first_character) - ord(second_character)
    print(f"#7. string={mystr}, third={first_character}, fifth={second_character}")
    print(f"chardiff={chardiff}\n")

# 8
first_number = 12
second_number = 25
third_number = 18
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number
print(f"#8. numbers={first_number}, {second_number}, {third_number}")
print(f"largest number={largest_number}\n")

# 9
water_temperature = 72
if water_temperature <= 32:
    print(f"#9. water temperature={water_temperature} F, state=freezing\n")
elif water_temperature >= 212:
    print(f"#9. water temperature={water_temperature} F, state=boiling\n")
else:
    print(f"#9. water temperature={water_temperature} F, state=liquid\n")

# 10
x = 5
if x >= 1 and x < 10:
    print(f"#10. x={x}")
