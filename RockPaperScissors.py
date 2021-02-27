import random
import sys

def maingame():
    human_score = 0
    computer_score = 0

    print('''=============================================================================================================================================================
                                                                 ABIR AL MAHDI PRESENTS...
                                                                Rock Paper Scissors Game!''')
    print(
        '=============================================================================================================================================================')
    print()
    print()
    name = input('Enter your name:  ')

    def scorer():

        global computer_score
        global human_score
        global name

    for i in range(10):

        human_choice = input('''Enter 'R' for Rock,
          'P' for Paper 
          'S' for Scissor: ''')

        choice_list = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choice_list)

        print()
        if human_choice == 'r' and computer_choice == 'Scissors':
            human_score = human_score + 1
            print('HUMAN SCORES!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 'p' and computer_choice == 'Scissors':
            computer_score = computer_score + 1
            print('COMPUTER SCORES!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 's' and computer_choice == 'Scissors':
            print('TIE!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 'r' and computer_choice == 'Paper':
            computer_score = computer_score + 1
            print('COMPUTER SCORES!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 'p' and computer_choice == 'Paper':
            print('Tie!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 's' and computer_choice == 'Paper':
            human_score = human_score + 1
            print('HUMAN SCORES!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 'r' and computer_choice == 'Rock':
            print('Tie!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 'p' and computer_choice == 'Rock':
            human_score = human_score + 1
            print('HUMAN SCORS!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()

        elif human_choice == 's' and computer_choice == 'Rock':
            computer_score = computer_score + 1
            print('COMPUTER SCORES!')
            print('Computer: ' + str(computer_choice))
            print('Computer score: ' + str(computer_score))
            print('Your score: ' + str(human_score))
            print()


    if human_score>computer_score:
        print('Congratulations, ' + name + '!' ' You won.')
    elif computer_score>human_score:
        print('Ahh, ' + name + '!' + ' You lose...')
    else:
        print('Its a tie!')

maingame()


def restart():
    restart = input('Do you want to play again? Enter Y for Yes and N for No: ')
    if restart == 'y':
        maingame()
    elif restart == 'n':
        sys.exit('Thanks for playing!')

res = 1
while res == 1:
    restart()

maingame()










