import sys
import random


# pyFileName, minNum, maxNum = sys.argv
# minNum = int(minNum)
# maxNum = int(maxNum)
# randomNum = random.randint(minNum, maxNum)
#
# while True:
#     try:
#         guessedNum = int(input(f'Pick a number between {minNum} and {maxNum}'))
#
#         if guessedNum > maxNum or guessedNum < minNum:
#             print(f'Your input cannot be less than {minNum} and greater than {maxNum}')
#             continue
#
#         if randomNum == int(guessedNum):
#             print('Whoohoo!! You found it!')
#             break
#         print('Wrong... Try again...')
#     except ValueError:
#         print('Wrong... Try again...')

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, i said 1~10')
        return False



if __name__ == '__main__':
    minNum = 1
    maxNum = 10
    randomNum = random.randint(minNum, maxNum)
    while True:
        try:
            guessedNum = int(input(f'Pick a number between 1 and 10'))
            if (run_guess(guessedNum, randomNum)):
                break
        except ValueError:
            print('Wrong... Try again...')



