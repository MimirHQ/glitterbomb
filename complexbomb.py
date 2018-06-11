from glitterbomb import (
    detonate,
    disarm
)


print('The bomb has three wires:')
print('a - red wire')
print('b - blue wire')
print('c - yellow wire')
wire = input('Enter the letter of the wire to cut: ')
if wire == 'c':
    print('The bomb has a keypad.')
    keypad_value = input('Enter a single number into the keypad: ')
    if not keypad_value.isnumeric():
        detonate()
    if len(keypad_value) > 1:
        detonate()
    number = int(keypad_value)
    if (number - 7) % 3 == 0:
        disarm()
    detonate()
else:
    detonate()
