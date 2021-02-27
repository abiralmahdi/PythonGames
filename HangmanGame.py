import random, turtle
a = turtle.Turtle()

def attempt1():
    a.penup()
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.pendown()

    a.left(180)
    a.forward(250)
    a.left(90)
    a.forward(100)


def attempt2():
    #attempt1()
    a.left(90)
    a.penup()
    a.forward(50)
    a.right(90)
    a.forward(7)
    a.pendown()
    a.circle(20)

def attempt3():
    #attempt2()
    a.left(90)
    a.penup()
    a.forward(40)
    a.pendown()
    a.forward(100)

def attempt4():
    #attempt3()
    a.back(80)
    a.right(45)
    a.forward(30)
    a.back(30)

def attempt5():
    #attempt4()
    a.left(90)
    a.forward(30)
    a.back(30)

def attempt6():
    #attempt5()
    a.right(45)
    a.forward(80)
    a.right(45)
    a.forward(40)
    a.back(40)

def attempt7():
    #attempt6()
    a.left(90)
    a.forward(40)
    a.back(40)

def attempt8():
    #attempt7()
    a.right(45)
    a.back(100)
    a.penup()
    a.back(40)
    a.pendown()
    a.back(50)
    a.left(90)
    a.forward(20)

print('==============================================================================================================')
print('                               Abir Al Mahdi Akhand Presents... The Hangman Game                              ')
print('==============================================================================================================')




attempt = 0
blank_list = []
list_of_words = ['apple', 'banana', 'mango', 'buffallo', 'tiger']
word_select = random.choice(list_of_words)

for i in range(len(word_select)):
    blank_list.append('_')

print('the word has ' + str(len(word_select)) + 'letters in it. ')
print(blank_list)

while 1:
    print()
    ans = input('Enter your guess : ')
    if ans in word_select:
        print()
        print('Correct Guessing!')
        for idx, letter in enumerate(word_select):
            if letter == ans:
                blank_list[idx] = word_select[idx]
        print(blank_list)
    elif ans not in word_select:
        attempt = attempt + 1
        print()
        print('Wrong guess!')
        print()
        print('Attempts remaining :' + str((8 - attempt)))
        print()
        print(blank_list)

        if attempt == 1:
            attempt1()
        
        elif attempt == 2:
            attempt2()
        
        elif attempt == 3:
            attempt3()
        
        elif attempt == 4:
            attempt4()
        
        elif attempt == 5:
            attempt5()
        
        elif attempt == 6:
            attempt6()
        
        elif attempt == 7:
            attempt7()
        
        elif attempt == 8:
            attempt8()
            print()
            print('You have lost the game!')
            break
        else:
            pass

    if '_' not in blank_list:
        print()
        print('You win!')
        break






