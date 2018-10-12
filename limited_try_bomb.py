"""
an example of bomb limited by number of attempts
"""
from glitterbomb import GlitterBomb


bomb = GlitterBomb(name="limited", prompt_limit=5)
secret_number = 42
while 1:
    decision = int(bomb.prompt("Try a number, 0-99: "))
    if decision == secret_number:
        bomb.disarm()
