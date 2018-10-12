"""
glitterbomb module
"""
import sys
import time
from random import choice


CONSOLE_WIDTH = 80
PLAIN_MODE_LIMIT = 5
RESET = "\033[0m"
PIECES = "abcdefghijklmnopqrstucwxyz0123456789!@#$%^&*()"


STRINGS = {
    "english": {
        "win": "You did it! :)",
        "disarmed": "The glitter bomb was safely disarmed",
        "detonated": "The glitter bomb detonated!",
        "spacer": "...",
    }
}


class Colors:
    """colors dataclass"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    LIGHTGREY = "\033[37m"
    DARKGREY = "\033[90m"
    LIGHTRED = "\033[91m"
    LIGHTGREEN = "\033[92m"
    YELLOW = "\033[93m"
    LIGHTBLUE = "\033[94m"
    PINK = "\033[95m"
    LIGHTCYAN = "\033[96m"

    @staticmethod
    def random():
        """gets a random color value"""
        options = [v for k, v in dict(vars(Colors)).items() if k[0:2] != "__"]
        return choice(options)


class GlitterBomb:
    """the glitter bomb class"""

    def __init__(
        self,
        name="glitterbomb",
        prompt_limit=-1,
        print_limit=-1,
        time_limit=-1,
        language="english",
    ):
        """glitter bomb constructor"""
        if language not in STRINGS:
            raise Exception("unsupported language")
        self.start_time = time.time()
        self.name = name

        self.print_count = 0
        self.prompt_count = 0
        self.print_limit = print_limit
        self.prompt_limit = prompt_limit
        self.time_limit = time_limit
        self.print_limited = self.print_limit != -1
        self.prompt_limited = self.prompt_limit != -1
        self.time_limited = self.time_limit != -1

        self.language = language
        self.plain_mode = False
        if len(sys.argv) >= 2:
            self.plain_mode = sys.argv[1] == "plain"

    def __repr__(self):
        """repl representation for this glitterbomb"""
        return "<GlitterBomb[{}]: {}>".format(id(self), self.name)

    @property
    def time_active(self):
        """gives a readout of how long the bomb has been active for"""
        return time.time() - self.start_time

    def detonate(self):
        """detonates the glitter bomb"""
        for m in range(PLAIN_MODE_LIMIT if self.plain_mode else CONSOLE_WIDTH):
            explosion = ""
            for n in range(CONSOLE_WIDTH):
                explosion += (
                    "*"
                    if self.plain_mode
                    else "{}{}{}".format(Colors.random(), choice(PIECES), RESET)
                )
            print(explosion)
        print(STRINGS[self.language]["spacer"])
        print(STRINGS[self.language]["detonated"])
        sys.exit(1)

    def disarm(self):
        """successfully disarms the glitter bomb"""
        duration = time.time() - self.start_time

        # if we took to long to disarm - detonate
        if self.time_limited and self.time_limit > duration:
            self.detonate()

        print(STRINGS[self.language]["spacer"])
        if self.plain_mode:
            print(STRINGS[self.language]["win"])
            print("{}!".format(STRINGS[self.language]["disarmed"]))
        else:
            print(Colors.LIGHTGREEN + STRINGS[self.language]["win"] + RESET)
            print(
                "{} in {0:.3f} seconds!".format(
                    STRINGS[self.language]["disarmed"], duration
                )
            )
        sys.exit(0)

    def prompt(self, text):
        """prompts the user for input"""
        self.prompt_count += 1
        if self.prompt_limited and self.prompt_count > self.prompt_limit:
            self.detonate()
        return input(text)

    def print(self, text):
        """prints text to the user"""
        self.print_count += 1
        if self.print_limited and self.print_count > self.print_limit:
            self.detonate()
        return print(text)


if __name__ == "__main__":
    print("Warning: this is not a glitter bomb you can play.")
