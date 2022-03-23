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

    def __str__(self):
        result = str(self.solution) + "\n" + str(self.current) + "\n" + str(self.wrong_guesses) + "\n" + str(self.status)
        return result


def check_word(word, board):
    if word == board.solution:
        board.current = board.solution
        return True
    if word not in board.wrong_guesses:
        board.wrong_guesses.append(word)
    return False


def check_char(c, board):
    if c not in board.solution:
        if c not in board.wrong_guesses:
            board.wrong_guesses.append(c)
        return False
    for i in range(len(board.solution)):
        if board.solution[i] == c:
            board.current = board.current[:i] + c + board.current[i + 1:]
    return True


def check_status(board):
    if len(board.wrong_guesses) >= 12:
        board.status = StatusType.lose
    elif board.current == board.solution:
        board.status = StatusType.win


def check_input(guess, board):
    if len(guess) != 1:
        result = check_word(guess, board)
    else:
        result = check_char(guess, board)
    check_status(board)
    return result

