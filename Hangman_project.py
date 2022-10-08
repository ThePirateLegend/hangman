import random
class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ("_"*len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        print(self.guess)
        if self.guess in self.word and self.guess not in self.list_of_guesses:
            print("Good guess!", self.guess, "is in the word")
            for i in range(len(self.word)):
                if self.word[i] == self.guess:
                    self.word_guessed = self.word_guessed[:i] + self.guess + self.word_guessed[i+1:]
            print(self.word_guessed)
            self.num_letters = self.num_letters-1
        elif self.guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            print("Sorry,", self.guess, "is not in the word.")
            self.num_lives = (self.num_lives)-1
            self.draw_hangman(self.num_lives)
            print("You have", self.num_lives, "lives left")
        self.list_of_guesses.append(self.guess)

    def ask_for_input(self):
        print(self.word_guessed)
        while self.num_lives != 0 and self.num_letters != 0:
            self.guess = input("guess a letter!")
            if (len(self.guess) != 1):
                print("Invalid letter. Please, enter a single alphabetical character."),
            else:
                self.check_guess(self.guess)
        if self.num_letters == 0:
                print("You win!")
        else:
            self.draw_hangman(self.num_lives)
            print("You lose!")

    def draw_hangman(self, num_lives):
        if self.num_lives == 4:
            print("/ \\")
        elif self.num_lives == 3:
            print("[ ]\n""/ \\")
        elif self.num_lives == 2:
            print(" [ ]\\ \n"" / \\")
        elif self.num_lives == 1:
            print("/[ ]\\ \n"" / \\")
        else:
            print("  O \n""/[ ]\\ \n"" / \\")


word_list = ["banana","apple","pineapple","pomegranite","blueberry","apricot","cucumber","carrot","broccoli"]
game = Hangman(word_list)
game.ask_for_input()
