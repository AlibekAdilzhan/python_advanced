# Write a game, where the user has to guess a word
import numpy as np


hint_word = {'computer' : ['What would you use to play Doom-2', 'компьютер in english', 'com*uter', 'computer'], 
            'himalaya' : ['What mountain is the highest', 'Lamas live there', 'Dzhamalungma 8848m', 'himala*a', 'Go to school and study geography' ], 
            'BMW' : ['Which is better BMW or Mersedes', 'Surely not mersedes', 'there are 3 letters?!', 'bmw is better'],
            '0' : ['1 + 1 = ?', 'where', 'I did not say anything about the ring', '0']}

we_want_to_play = int(input('do you want to play? (0/1): '))

print('The game is started')

while we_want_to_play == 1:
    question_number = np.random.randint(0, len(hint_word))

    points = [0, 0]

    the_word = list(hint_word.keys())[question_number]
    hints = hint_word[the_word]

    game_over = False
    letter_in_word = False
    board = list("*" * len(the_word))

    k = 0 # number of hint
    j = 0 # player0 or player1
    rounds = len(board) # number of iterations, to stop the game if the word was guessed

    the_word = the_word.lower()

    while not game_over:
        k = k % len(hints)
        j = j % 2
        hint = hints[k]
        if rounds != 0:
            print("------------------------------")
            potential_points = np.random.randint(100, 1001) # points that is going to be added to the person who will guess the letter/word
            print(f'Player{j} have {points[j]} points, do your best!')
            print(f"Potential points are {potential_points}\n")
            print(f"Guess a word: {' '.join(board)}\n")
            print(f"Hint: {hint}\n")
            user_guess = input("Enter a word or a letter: ")
            user_guess = user_guess.lower()
            if len(user_guess) == 1:
                letter_in_word = False
                for i in range(len(the_word)):
                    if the_word[i] == user_guess:
                        board[i] = user_guess
                        letter_in_word = True
                        rounds -= 1 # every right guess decreases the number of rounds by 1

                if letter_in_word == True:
                    points[j] += potential_points # if the playerj guessed the word right he/she will get points
                    print(f'Very well! player{j} now have {points[j]} points')

                else:
                    print(f'Try better, player{j}, you can do this! (maybe)')
                    j += 1
                    k += 1

            else:
                if user_guess == the_word:
                    print("Correct! Congratulations! The game has been ended")
                    points[j] = potential_points * rounds
                    rounds = 0
                    game_over = True

                else:
                    points[j] -= potential_points * rounds * 0.5
                    print(f"Incorrect, think again, for the naglost' player{j} loses {potential_points * rounds * 0.5} points, now he/she have {points[j]} points")
                    j += 1
                    k += 1
                
            letter_in_word = False

        else:
            game_over = True

    print('\n\n')


    if points[0] > points[1]:
        print(f'Player0 wins with {points[0]} points')

    elif points[0] == points[1]:
        print(f'Friendship wins with {points[0]} points')

    else:
        print(f'Player1 wins with {points[1]} points')

    we_want_to_play = int(input('do you want to play again? (0/1): '))

print('\nokaaay (')

# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.