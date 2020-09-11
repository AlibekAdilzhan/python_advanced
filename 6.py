# Write a game, where the user has to guess a word
import numpy as np


hint_word = {'computer' : ['What would you use to play Doom-2', 'компьютер in english', 'com*uter', 'computer'], 
            'himalaya' : ['What mountain is the highest', 'Lamas live there', 'Dzhamalungma 8848m', 'himala*a', 'Go to school and study geography' ], 
            'BMW' : ['Which is better BMW or Mersedes', 'Surely not mersedes', 'are there 3 letters?!', 'bmw is better'],
            '0' : ['1 + 1 = ?', 'where', 'I did not say anything about the ring', '0'],
            'Mariana' : ['The deepest place in the world', '11022m', 'Ma*****', 'Mariana'],
            'Jupyter' : ['The closest to the Sun planet', '******* notebook', 'Jup****', 'Jupyter'],
            'Hiruzen' : ['The 3rd hokage', 'old man']}

persuades = ["The sum is quite big, so choose the money", "Wouldn't you be disappointed if there is a just book",
            "Oooh, man, you are crazy if you refuse from such a bag of money", "Yes there might be a car, but is it more valuable than this money",
            "What if there is a pen", "Hmmm, I can understand you, everyone is waiting for the miracle, but the mathematical expectation is very small!",
            "Won't you regret, my friend?", "The last chance to choose the money"]

prizes_valuable = ['bmw x7', 'house', 'penthouse', 'toyota 80', 'planet', 'diamond'][
prizes_not_valuable = ['pen', 'pencil', 'pineapple', 'brelok']


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
            if np.random.randint(0, 21) % 11 == 0:
                print(f"What a luckyness. player{j} have a chance to win a really good thing or take really big money!")
                number_of_persuades = np.random.randint(3, len(persuades)) # how many times I should ask to choose the money!
                money = 1000000
                if np.random.randint(0, 21) % 2 == 0: # The chance is 50/50 (either something valuable or not)
                    random_prize_valuable = np.random.randint(0, len(prize_valuable))   # deciding what prize to give
                    prize = prizes[random_prize_valuable]
                else:
                    random_prize_not_valuable = np.random.randint(0, len(prizes_not_valuable))  # deciding what prize to give
                    prize = prizes_not_valuable[random_prize_not_valuable]
                for i in range(number_of_persuades):
                    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                    money = (i + 1) * money
                    if i == 0:
                        print(f'I suggest you {money} points. {persuades[i]}. You can choose a prize as well')
                    else:
                        print(f'This time {money} points are almost in your hands. {persuades[i]}. What is your choise?')
                    
                    prize_or_money = int(input('Prize or Money (0/1): '))
                    
                    if prize_or_money == 1:
                        break
                
                if prize_or_money == 0:
                    if potential_points % 2 == 0:
                        print(f"UUU, I knew that you are lucky. Congratulations!. Now you have bmw x7 and {points[j]} points. Let's continue the game!")
                    else:
                        print("I TOLD YOU! I TOLD you to choose the money. Oooh, you are really a crazy man! Okay, it's not the end. Let's continue the game!")

                else:
                    points[j] += money
                    print(f"Okay, man, this is quite well too. You have now {points[j]} points") #AAAAAAAAAAAAAAAAAAAAAAAAAAAA

            # else:
            print(f'Player{j} have {points[j]} points, do your best!')
            print(f"Potential points are {potential_points}\n")
            print(f"Guess a word: {' '.join(board)}\n")
            print(f"HINT: {hint}\n")
            user_guess = input("Enter a word or a letter: ")
            user_guess = user_guess.lower()
            if len(user_guess) == 1:
                letter_in_word = False
                for i in range(len(the_word)):
                    if the_word[i].lower() == user_guess.lower() and board[i] == '*':
                        board[i] = user_guess
                        letter_in_word = True
                        rounds -= 1 # every right guess decreases the number of rounds by 1

                if letter_in_word == True:
                    points[j] += potential_points # if the playerj guessed the word right he/she will get points
                    print(f'CORRECT!, Very well! player{j} now have {points[j]} points')

                else:
                    print(f'INCORRECT!, Try better, player{j}, you can do this! (maybe)')
                    if j == 1:
                        k += 1
                    j += 1

            else:
                if user_guess == the_word:
                    print("CORRECT! Congratulations! the word was guessed")
                    points[j] = potential_points * rounds
                    rounds = 0
                    game_over = True

                else:
                    points[j] -= potential_points * rounds * 0.5
                    print(f"INCORRECT, think again, for the naglost' player{j} loses {potential_points * rounds * 0.5} points, now he/she have {points[j]} points")
                    if j == 1:
                        k += 1
                    j += 1
                
            letter_in_word = False

        else:
            game_over = True

    print('\n----GAME RESULTS----\n')

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