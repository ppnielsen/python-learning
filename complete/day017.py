'''
Day 17 of Cup of Code's Python tutorial
Dragon Project: How to Fend Off a Dragon
'''

def dragon_game():
    '''
    Select a good or bad dragon! Will you guess right?
    '''

    import random
    import time

    # Creating our own functions so we can call the code and not have to keep writing it

    def display_intro():
        '''
        Shows the intro of the game
        '''

        print('You are in a land full of dragons')
        time.sleep(2)
        print('''In front of you, you can see two caves.
In one cave, the dragon is nice! He will share gold with you!
The other dragon is greedy and hungry and will eat you on site!''','\n')

    def choose_cave():
        '''
        Choosing the cave that will determine your fate!
        '''

        cave = ''
        while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()

        return cave

    def check_cave(picked):
        '''
        Checking to see if the cave was good or not
        '''

        print('You approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps in front of you! He opens his jaws and...')
        print()
        time.sleep(4)

        friendly_cave = random.randint(1, 2)

        if picked == str(friendly_cave):
            print('He gives you treasure!')
        else:
            print('He gobbles you down in one bite!')

    play_again = 'yes'

    while play_again == 'yes' or play_again == 'y':
        display_intro()
        cave_nbr = choose_cave()
        check_cave(cave_nbr)

        print('Do you want to play again? (yes or no)')
        play_again = input()

dragon_game()
