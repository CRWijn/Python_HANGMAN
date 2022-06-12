import random
import os

class start_hangman:

    def __init__(self):
        self.hangman_matrix = [
            [' ', '_', '_', '_', '_', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', 'O', ' '],
            [' ', '|', ' ', '/', '|', '\\'],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', '/', ' ', '\\'],
            [' ', '|', ' ', ' ', ' ', ' '],
            ['-', '-', '-', '-', '-', '-']
            ]

        self.output_matrix = [
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']
            ]
        
        self.errors_made = 0
        self.guessed_letters = []
        self.word = self.get_word()
        self.word_status = []
        for ndx in range(0, len(self.word)):
            self.word_status.append('-')
        if self.input_loop():
            print("You won!")
        else:
            print("You lost!")

    def input_loop(self):
        game_over = False
        while (not game_over):
            os.system("CLS")
            self.print_game_status()
            guess = input("Guess a letter or word: ").lower()
            if len(guess) > 1:
                if guess == self.word:
                    self.update_output(False, guess, guess)
                    self.print_game_status()
                    return True
                else:
                    self.errors_made += 1
                    self.update_output(True, guess, guess);
            else:
                if 97 <= ord(guess) <= 122:
                    if guess in self.guessed_letters:
                        continue
                    elif guess in self.word:
                        self.update_output(False, guess)
                    else:
                        self.errors_made += 1
                        self.update_output(True, guess)

            if self.errors_made == 7:
                os.system("CLS")
                self.update_output(False, self.word, self.word)
                self.print_game_status()
                return False
            elif "".join(self.word_status) == self.word:
                os.system("CLS")
                self.update_output(False, self.word, self.word)
                self.print_game_status()
                return True
                        

    def print_game_status(self):
        for row in self.output_matrix:
            output_line = '';
            for col in row:
                output_line += col;
            print(output_line)
        print('Guessed Letters: ' + "".join(self.guessed_letters))
        print('Your Word: ' + "".join(self.word_status))

    def get_word(self):
        with open('words.txt') as f:
            num_words = sum(1 for line in f)
            word_int = random.randint(0, num_words-1)
            f.seek(0)
            for ndx, content in enumerate(f):
                if ndx == word_int:
                    return content.strip()

    def update_output(self, is_error, inp, word = ''):
        
        error_dict = {
            1: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5)],
            2: [(6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)],
            3: [(0, 1), (0, 2), (0, 3), (0, 4)],
            4: [(1, 4), (2, 4)],
            5: [(3, 4), (4, 4)],
            6: [(3, 3), (3, 5)],
            7: [(5, 3), (5, 5)]
            }
        
        if is_error:
            for coord in error_dict[self.errors_made]:
                    self.output_matrix[coord[0]][coord[1]] = self.hangman_matrix[coord[0]][coord[1]]
            if word == '' and self.errors_made < 7:
                self.guessed_letters.append(inp)
        else:
            if word != '':
                for ndx, letter in enumerate(self.word):
                    self.word_status[ndx] = letter
            else:
                for ndx, letter in enumerate(self.word):
                    if letter == inp:
                        self.word_status[ndx] = letter
    

while (1):
    play = input("Play y/n?").lower()
    if play == 'y':
        temp = start_hangman()
    else:
        break
