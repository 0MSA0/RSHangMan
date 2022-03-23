import json
import random


class StatusType:
    running = 0
    win = 1
    lose = 2


class Board:
    solution = ""
    current = ""
    wrong_guesses = []
    status = StatusType.running

    def __init__(self):
        file = open("words.json", "r")
        content = file.read()
        words = json.loads(content)
        word_id = random.randint(0, len(words) - 1)

        self.solution = words[word_id]
        for c in self.solution:
            if c == " ":
                self.current += " "
            else:
                self.current += "_"
