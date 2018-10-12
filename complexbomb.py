"""
an example of a more complex bomb
"""
from glitterbomb import GlitterBomb


bomb = GlitterBomb(name="complex")
bomb.print("The bomb has three wires:")
bomb.print("a - red wire")
bomb.print("b - blue wire")
bomb.print("c - yellow wire")
wire = bomb.prompt("Enter the letter of the wire to cut: ")
if wire == "c":
    bomb.print("The bomb has a keypad.")
    keypad_value = bomb.prompt("Enter a single number into the keypad: ")
    if not keypad_value.isnumeric():
        bomb.detonate()
    if len(keypad_value) > 1:
        bomb.detonate()
    number = int(keypad_value)
    if (number - 7) % 3 == 0:
        bomb.disarm()
    bomb.detonate()
else:
    bomb.detonate()
