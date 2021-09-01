
import random
import os

def clear_screen ():
    os.system('cls')


def get_input():
    
    while True:

        print('-'*15)
        user_input = input('plase choice your guess : ').lower()

        if user_input.isalpha():
            return user_input
        print('your input is not valid plase entar agin.')


def take_input_from_list (names):
    user_input = get_input()

    while user_input not in names:
        print('you should guess a word from the given word list.')
        print('please enter correct word.')
        user_input = get_input()

    return user_input

        
def game_info():
    print('-'*15)
    print('welcome to the game.')
    print(f'choice one name of list : {list_name}')
    


def run_game(number_of_guess , names):

    game_info()
    print(f'number of guess is :{number_of_guess}')
    select_random = random.choice(names)
    

    for i in range(number_of_guess):
        user_input = take_input_from_list(names)

        if user_input == select_random:
            return f'YOu WIN : {user_input} '

        else:
            print('your guessed wrong')
            print(f'please try agin. number of round left : {number_of_guess -1 - i}')

    print(f'you lost. the correct answer is : {select_random}')

list_name = ['james' , 'john' , 'jennifer' , 'elizabeth' , 'linda' , 'david' , 'richard']
clear_screen()
run_game(5 , list_name)
