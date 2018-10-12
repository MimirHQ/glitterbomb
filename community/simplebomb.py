"""
an example of a simple bomb
"""
from glitterbomb import GlitterBomb


bomb = GlitterBomb(name="simple")
secret_number = 5
bomb.print("The bomb has a knob.")
decision = bomb.prompt("Do you turn the knob? (yes/no): ")
if decision == "yes":
    secret_number += 3
elif decision == "no":
    secret_number -= 3
else:
    bomb.detonate()

guess = int(bomb.prompt("Enter the secret number: "))
if guess == secret_number:
    bomb.disarm()
bomb.detonate()
