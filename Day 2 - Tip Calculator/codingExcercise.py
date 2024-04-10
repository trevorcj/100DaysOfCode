# Coding Challenge 1
# #Write a program that adds the digits in a 2-digit number
# # Example:
# # input: 39
# # output: 12
# 
# # ask the user to enter a two-digit number
# two_digit_number = input('Enter a 2-digit number: ')
# 
# # add the first and second digit, take the input, convert it to an int
# two_digit_number = int(two_digit_number[0]) + int(two_digit_number[1])
# 
# # print the output
# print(two_digit_number)


# ////////////////////////////////////////////
# Coding Challenge 2

# Write a program that calculates a person's BMI (Body Mass Index)
# from their weight and height
# BMI = weight(kg) / height ** height(m2)
#
# input: height(1.75), weight(80)

# # ask user for their weight and height
# height = input('Enter height in meters e.g 1.65: ')
# weight = input('Enter weight in kilograms e.g 72: ')
# 
# # calculate their BMI
# height = float(height)
# weight = float(weight)
# 
# bmi = weight / (height ** 2)
# bmi = int(bmi)
# 
# # print the result
# print(bmi)
# print('Your BMI is ' + str(bmi) + 'kgm-2')


# ////////////////////////////////////////////
# Coding Challenge 3 (Your Life In Weeks)

# Write a program that tells us how many weeks we have left, if we live
# until 90 years old

# ask user for their age
age = input('How old are you: ')

#calculate how much time they have left in weeks
years = 90 - int(age)
lifeInWeeks = years * 52

# print it to the console
print(f'You have {lifeInWeeks} weeks left.')













