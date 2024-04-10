print('Welcome to the tip Calculator!')

# ask how much the total bill amounts to
bill = float(input('What was the total bill? '))

# ask how much tip they'd like to give
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))

# ask how many people should split the bill
people = int(input('How many people to split the bill? '))

# calculate the tip
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = float(total_bill / people)

# final_amount = round(bill_per_person, 2)
final_amount = '{:.2f}'.format(bill_per_person)

#print it to the console
print(f'Each person should pay: ${final_amount}')


