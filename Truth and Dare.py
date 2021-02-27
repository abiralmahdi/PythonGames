import turtle, random, sys, os

#def board_design():

print('================================================================================================================')
print('''                                               ABIR AL MAHDI Presents 
                                          The Ultimate Truth and Dare Game''')
print('================================================================================================================')
print()





def player_entry():

    truth_list = ['What are your top three turn-ons?',
'What is your deepest darkest fear?',
'Tell me about your first kiss?',
'Who is the sexiest person here?',
'What is your biggest regret?',
'Who here has the nicest butt?',
'Who is your crush?',
'Who was the last person you licked?',
'Have you ever cheated or been cheated on?',
'Tell me about your most awkward date?',
'Have you ever made out with someone here?',
'What are you most self-conscious about?',
'When was the last time you peed in bed?',
'What is the biggest lie you have ever told?',
'What is the most embarrassing picture of you?',
'Who is the person you most regret kissing?',
'Tell us your most embarrassing vomit story',
'What is the naughtiest thing you’ve done in public?',
'What do most people think is true about you, but isn’t?',
'What is the biggest thing you’ve gotten away with?',
'What would you do if you were the opposite sex for a month?',
'What is the most expensive thing you have stolen?',
'What is the most childish thing you still do?',
'What’s the worst time you let someone take the blame for something you did?',
'What is something your friends would never exect that you do?',
'Who here would you most like to make out with?',
'What lie have you told that hurt someone?',
'What is the meanest you have been to someone that didn’t deserve it?',
'What is something that people think you would never be into, but you are?',
'What was the worst encounter you had with a police officer?',
'What is the silliest thing you have an emotional attachment to?',
'Where is the strangest place you have peed?',
'Have you ever crapped your pants since you were a child?',
'What is the most embarrassing thing your parents have caught you doing?',
'What secret about yourself did you tell someone in confidence and then they told a lot of other people?',
'When was the most inappropriate time you farted?',
'What is the scariest dream you have ever had?',
'What is the most embarrassing thing in your room?',
'Why did you break up with your last boyfriend or girlfriend?',
'What is the stupidest thing you have ever done?',
'What is the grossest thing that has come out of your body?',
'What is your favorite thing that your boyfriend or girlfriend does?',
'What terrible thing have you done that you lied to cover up?',
'Who have you loved but they didn’t love you back?',
'What is something that you have never told anyone?',
'What is the most disgusting habit you have?',
'What pictures or videos of you do you wish didn’t exist?',
'What was the cruelest joke you played on someone?',
'What is the most embarrassing thing you have put up on social media?',
'What horrible thing have you done that no one else found out about?',
'What was the most awkward romantic encounter you have had?',
'What is the grossest thing you have had in your mouth?',
'Tell me about the last time someone unexpectedly walked in on you while you were naked?',
'What is the most embarrassing nickname you have ever had?',
'What is the most embarrassing series of texts you have on your phone?',
'Describe your most recent romantic encounter in detail?',
'What is the weirdest thing you have done for a boyfriend or girlfriend?',
'Is it true that you (whatever you or the group suspects they do / did)?',
'When was the last time you wiped a booger off on something that shouldn’t have boogers on it?',
'What do you really hope your parents never find out about?',
'Tell me something you don’t want me to know?',
'What have you done that people here would judge you most for doing?',
'If you starred in a romance, what would it be like?']

    ans_list = []

    dare_list = ['Serenade the person to your right,',
'Talk in an accent for the next  rounds,',
'Kiss the person to your left,',
'Attempt to do a magic trick,',
'Do four cartwheels in row,',
'Let someone shave part of your body,',
'Eat five tablespoons of a condiment,',
'Be someone’s pet for the next  minutes,',
'Sniff the armpits of everyone in the room,',
'Dance to a song of the group’s choosing.',
'Take a shower with your clothes on.',
'Break two eggs on your head.',
'Do your best impression of a baby being born.',
'Belly dance like your life depended on it.',
'Put  ice cubes down your pants.',
'Lick the floor.',
'For a guy, put on makeup. For a girl, wash off your make up.',
'Dance with no music for  minute.',
'Try to drink a glass water while standing on your hands.',
'Let the group pose you in an embarrassing position and take a picture.',
'Play a song on by slapping your butt cheeks till someone guesses the song.',
'Give someone your phone and let them send one text to anyone in your contacts.',
'Dare. Depict a human life through interpretive dance.',
'Drink a small cup or shot of a concoction that the group makes. (Don’t make anything that might cause bodily harm. No visits to the emergency room.).',
'Write or draw something embarrassing somewhere on your body (that can be hidden with clothing) with a permanent marker.',
'Make every person in the group smile, keep going until everyone has cracked a smiled.',
'Let the person to your left draw on your face with a pen.',
'Make up a 0 second opera about a person or people in the group and perform it.',
'Beg and plead the person to your right not to leave you for that other boy or girl. Weeping, gnashing of teeth, and wailing is encouraged.',
'Do pushups until you can’t do any more, wait  seconds, and then do one more.',
'Sell a piece trash to someone in the group. Use your best salesmanship.',
'Let the group look through your phone for  minute.',
'Imitate a celebrity every time you talk for three minutes.',
'Try to juggle  or  items of the group’s choosing.',
'Stick your arm into the trash can past your elbow.',
'Walk on your hands from one side of the room to the other. You can ask someone to hold your legs if necessary.',
'Gargle something that shouldn’t be gargled but won’t hurt you.',
'Get slapped on the face by the person of your choosing.',
'Grab a trash can and make a hoop with your hands above the trash can. Have other members of the group try to shoot trash through your impromptu trashketball hoop.',
'Spin an imaginary hula hoop around your waist for  minutes while the game continues.',
'Imitate popular YouTube videos until someone can guess the video you are imitating.',
'Seduce a member of the same gender in the group.',
'Compose a poem on the spot based on something the group comes up with.',
'Poll dance for  minute with an imaginary pole.',
'Attempt to walk on your elbows and knees for as far as you can.',
'Choose someone from the group to give you a spanking.',
'Post an extremely unflattering picture of yourself to the social media outlet of your choosing.',
'Make a funny face and keep making it for  minutes while the game continues.',
'Imagine something in your room. Now spell it with your nose and keep spelling it with your nose until someone from the group guesses what you are trying spell.',
'After the group chooses one word, sing a song and insert that word once into every line of the song.',
'Drag your butt on the carpet like a dog from one end of the room to the other.',
'Open a bag of snacks or candy using only your mouth, no hands or feet.',
'Bend at the waist so that you are looking behind you between your legs. Now run backwards until you can tag someone with your butt.',
'Make a tea out of something that isn’t tea (but is NOT dangerous or toxic) and drink it.',
'Go to the bathroom, take off your underwear and put it on your head. Wear it on your head for 0 minutes.',
'Act like whatever animal someone yells out for the next  minute.',
'Eat one teaspoon of the spiciest thing you have in the kitchen.',
'Transfer an ice cube from the person on the right’s mouth to yours.',
'Call the th contact in your phone and sing them 0 seconds of a song that the group chooses.',
'No talking. Pretend to be a food. Don’t pretend to eat the food, pretend to be the food. Keep pretending until someone in the group guesses the food you are.',
'Drop something in the toilet and then reach in to get it.',
'Find the person whose first name has the same letter as your first name or whoever’s first name’s first letter is closest to yours. Now lick their face or let them lick your face, their choice.',
'Sit in a spinning chair and have the group spin you for 0 seconds. Might help to hold a trash can just in case.',
'Jump up and down as high as you can go for a full minute.',
'Let two people give you a wet willy at the same time.',
'Sing a praise song about a person of the groups choosing.']

    dare_done_list = []

    while True:
        player_list = []

        no_of_players = int(input('Enter the number of players : '))
        n = 0
        for i in range(no_of_players):
            n = n+1
            name = input('Enter the name of the player' + str(n) + ' : ')
            player_list.append(name)
        #print(player_list)

        while True:

            round = input('Press S to start toss or E to Exit the game : ')

            if round == 's':
                toss = random.choice(player_list)
                print()
                print(toss)
                print()

                t_d = input('Enter T for Truth and D for Dare : ')
                if t_d == 't':
                    print(toss + ' has chosen Truth!')
                    ques = random.choice(truth_list)
                    print()
                    print('Your Question is : ' + ques)
                    ans = input('Your Answer : ')
                    ans_list.append(ques + ' Ans : ' + ans)

                elif t_d == 'd':
                    print(toss + ' has chosen Dare!')
                    dare = random.choice(dare_list)
                    print()
                    print('Your Question is : ' + dare)
                    dare_done = input('Your Answer : ')
                    dare_done_list.append(dare + ' Ans : ' + dare_done)

            elif round == 'e':
                print()
                sys.exit('Thanks for playing this game!')


player_entry()






