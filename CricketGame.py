import random
import sys

global wicket
global human_score
global computer_score
global humanwicket
human_score = 0
wicket = 0
computer_score = 0
humanwicket = 0


def player_bat1():
    global human_score
    global wicket


    human_score = 0
    wicket = 0


    for i in range(100):
        human_shot = int(input('Enter your run (0/1/2/3/4/6) : '))
        computer_choice_list = [0, 1, 2, 3, 4, 6]
        computer_shot = random.choice(computer_choice_list)
        print()
        print()

        if human_shot == computer_shot:
            wicket = wicket+1
            print('Computer shots: ' + str(computer_shot))
            print('Out!')
            print('Human score: ' + str(human_score))
            print('Wicket: ' + str(wicket))
        elif human_shot != computer_shot:
            if human_shot == 0:
                human_score = human_score
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 1:
                human_score = human_score + 1
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 2:
                human_score = human_score + 2
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 3:
                human_score = human_score + 3
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 4:
                human_score = human_score + 4
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 6:
                human_score = human_score + 6
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))
            else:
                print('Error!')
        else:
            print('Error')

        if wicket == 3:
            print('All out!')
            player_bowl2()


def player_bowl1():

    global computer_score
    global humanwicket

    computer_score = 0
    humanwicket = 0


    for i in range(100):
        human_bowl = int(input('Bowl (0/1/2/3/4/6): ' ))
        computer_shot_choice = [0, 1, 2, 3, 4, 6]
        computer_shot = random.choice(computer_shot_choice)
        print()
        print()

        if human_bowl == computer_shot:
            humanwicket = humanwicket + 1
            print('Computer shots: ' + str(computer_shot))
            print('Out!')
            print('Computers score : ' + str(computer_score))
            print('Wicket: ' + str(humanwicket))

        elif human_bowl != computer_shot:
            if computer_shot == 0:
                computer_score = computer_score
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 1:
                computer_score = computer_score + 1
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 2:
                computer_score = computer_score + 2
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 3:
                computer_score = computer_score + 3
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 4:
                computer_score = computer_score + 4
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 6:
                computer_score = computer_score + 6
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            else:
                print('Error!')
        else:
            print('Error!')

        if human_bowl >6:
            print('Your bowl limit is upto 6!')

        if humanwicket == 3:
            print('All out!')
            player_bat2()


def player_bowl2():
    computer_score = 0
    humanwicket = 0

    def scorer():
        global computer_score
        global humanwicket

    for i in range(100):
        human_bowl = int(input('Bowl (0/1/2/3/4/6): ' ))
        computer_shot_choice = [0, 1, 2, 3, 4, 6]
        computer_shot = random.choice(computer_shot_choice)
        print()
        print()

        if human_bowl == computer_shot:
            humanwicket = humanwicket + 1
            print('Out!')
            print('Computer shots: ' + str(computer_shot))
            print('Computers score : ' + str(computer_score))
            print('Wicket: ' + str(humanwicket))

        elif human_bowl != computer_shot:
            if computer_shot == 0:
                computer_score = computer_score
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 1:
                computer_score = computer_score + 1
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 2:
                computer_score = computer_score + 2
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 3:
                computer_score = computer_score + 3
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 4:
                computer_score = computer_score + 4
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            elif computer_shot == 6:
                computer_score = computer_score + 6
                print('Computer shots: ' + str(computer_shot))
                print('Computers score : ' + str(computer_score))
                print('Wicket: ' + str(humanwicket))

            else:
                print('Error!')
        else:
            print('Error!')

        if human_bowl >6:
            print('Your bowl limit is upto 6!')
        if humanwicket == 3:
            print('All out!')
            if computer_score > human_score :
                print('You lose!')
            elif computer_score < human_score:
                print('You won!')
            else:
                print('Tie!')

                exit = input('Do you want to play again? Press Y to play again and N to exit: ')
                if exit == 'n':
                    sys.exit('Thanks for playing. ')
                elif exit == 'y':
                    toss()
                else:
                    print('Error!')
                    sys.exit('BYE')

        if computer_score > human_score :
            print('You lose!')

            exit= input('Do you want to play again? Press Y to play again and N to exit: ')
            if exit == 'n':
                sys.exit('Thanks for playing. ')
            elif exit == 'y':
                toss()
            else:
                print('Error!')
                sys.exit('BYE')


def player_bat2():

    global human_score
    global wicket

    human_score = 0
    wicket = 0

    for i in range(100):
        human_shot = int(input('Enter your run (0/1/2/3/4/6) : '))
        computer_choice_list = [0, 1, 2, 3, 4, 6]
        computer_shot = random.choice(computer_choice_list)
        print()
        print()

        if human_shot == computer_shot:
            wicket = wicket+1
            print('Out!')
            print('Human score: ' + str(human_score))
            print('Wicket: ' + str(wicket))
        elif human_shot != computer_shot:
            if human_shot == 0:
                human_score = human_score
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 1:
                human_score = human_score + 1
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 2:
                human_score = human_score + 2
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 3:
                human_score = human_score + 3
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 4:
                human_score = human_score + 4
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))

            elif human_shot == 6:
                human_score = human_score + 6
                print('Computer shots: ' + str(computer_shot))
                print('Human score: ' + str(human_score))
                print('Wicket: ' + str(wicket))
            else:
                print('Error!')
        else:
            print('Error')

        if wicket == 3:
            print('All out!')
            if computer_score > human_score :
                print('You lose!')
            elif computer_score < human_score:
                print('You won!')
            else:
                print('Tie!')

                exit = input('Do you want to play again? Press Y to play again and N to exit: ')
                if exit == 'n':
                    sys.exit('Thanks for playing. ')
                elif exit == 'y':
                    toss()
                else:
                    print('Error!')
                    sys.exit('BYE')

        if computer_score > human_score:
            print('You lose!')
            exit = input('Do you want to play again? Press Y to play again and N to exit: ')
            if exit == 'n':
                sys.exit('Thanks for playing. ')
            elif exit == 'y':
                toss()
            else:
                print('Error')
                sys.exit('BYE')



def toss():
    print()
    print()
    print('=============================================================================================================')
    print('''                                        ABIR AL MAHDI PRESENTS:                                                
                               The Head-Tails Mini-Cricket game - 2020                                   ''')
    print('Welcome!')
    computer_choice_list = ['Computer chooses to bat first!', 'Computer chooses to bowl first!']
    head_tail = ['h', 't']
    destiny = random.choice(head_tail)
    computer_choice = random.choice(computer_choice_list)

    toss = input('''Its toss time! 
    What do you wanna choose? 
    Press H for Heads and T for Tails:  ''')
    print()

    if toss == destiny:
        print('Computer tosses: ' + destiny)
        print()
        print('You have won the toss. ')
        print()
        human_choice = input('What would you like to choose? Press B for Batting and F for Fielding:   ')
        print()
        if human_choice == 'b':
            player_bat1()
        elif human_choice == 'f':
            player_bowl1()

    else:
        print('Computer tosses: ' + destiny)
        print()
        print('You have lost the toss! ')
        print()
        print(computer_choice)
        print()

        if computer_choice == 'Computer chooses to bat first!':
            player_bowl1()
        elif computer_choice == 'Computer chooses to bowl first!':
            player_bat1()



# SO, LETS START THE GAME!!!

toss()






