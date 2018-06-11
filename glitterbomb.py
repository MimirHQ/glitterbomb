from random import choice as random_choice
from time import time as get_time
import sys

console_width = 80
reset = '\033[0m'
pieces = 'abcdefghijklmnopqrstucwxyz0123456789!@#$%^&*()'
colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'lightgrey': '\033[37m',
    'darkgrey': '\033[90m',
    'lightred': '\033[91m',
    'lightgreen': '\033[92m',
    'yellow': '\033[93m',
    'lightblue': '\033[94m',
    'pink': '\033[95m',
    'lightcyan': '\033[96m'
}

start_time = get_time()
plain_mode = False
if len(sys.argv) >= 2:
    plain_mode = sys.argv[1] == 'plain'


def detonate():
    if plain_mode:
        for m in range(5):
            small_explosion = ''
            for n in range(console_width):
                small_explosion += '*'
            print(small_explosion)
    else:
        for i in range(console_width):
            explosion = ''
            for j in range(console_width):
                color = random_choice(list(colors.values()))
                glitter = random_choice(pieces)
                explosion += color + glitter + reset
            print(explosion)
    print('...')
    print('The glitter bomb detonated.')
    exit()


def disarm():
    duration = get_time() - start_time
    print('...')
    victory = 'You did it! :)'
    if plain_mode:
        print(victory)
        print('The glitter bomb was safely disarmed.')
    else:
        print(colors['lightgreen'] + victory + reset)
        print('The glitter bomb was safely disarmed in {0:.3f} seconds'.format(duration))
    exit()


if __name__ == '__main__':
    print('Warning: this is not a glitter bomb you can play.')
