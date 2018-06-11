from glitterbomb import (
    detonate,
    disarm
)

secret_number = 5
print('The bomb has a knob.')
decision = input('Do you turn the knob? (yes/no): ')
if decision == 'yes':
    secret_number += 3
elif decision == 'no':
    secret_number -= 3
else:
    detonate()

guess = input('Enter the secret number: ')
if guess == str(secret_number):
    disarm()
detonate()
