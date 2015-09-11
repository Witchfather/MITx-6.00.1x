"""
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search,
the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
"""

class GuessMachine(object):

    foundSecret = False
    high = 0
    low = 0
    g = 0

    def __init__(self, low=0, high=100):
        self.high = high
        self.low = low
        g = (high - low) / 2 #current guess

    def guess(self, answer):
        if (answer == 'h'):
            self.high = self.g
        elif (answer == 'l'):
            self.low = self.g
        elif (answer == 'c'):
            self.foundSecret = True
        else:
            return -1
        self.g = abs((self.low + self.high) / 2)
        return self.g

if __name__ == "__main__":
    gm = GuessMachine(0, 100)
    print ('Please think of a number between 0 and 100!')

    guess = gm.guess('l')
    while (gm.foundSecret == False):
        print('Is your secret number ' + str(guess)  + '?')
        r = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
        guess = gm.guess(r)
        if guess == -1:
            print 'Sorry, I did not understand your input.'
    print ('Game over. Your secret number was: ' + str(guess))
