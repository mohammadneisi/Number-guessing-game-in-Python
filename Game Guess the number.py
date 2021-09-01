
import string
import random
import os
def clear_screen ():
    os.system('cls')

def welcome_message_game_info():
    print('Welcome Guess The Number Game')
    print('-'*10,'     ','-'*10)
    
    # game_info()


def get_user_input(num_input1 , num_input2 , get_random_number):
    number_repetiton = 0
    while True:
        print('-'*15)
        user_input = input(f'enter the choice number from :{num_input1} at {num_input2} : ')

        if user_input.isdigit():
            user_input = int(user_input)
            
            number_repetiton+=1
            if user_input < get_random_number:
                print('Try Again! You guessed too small:' , user_input)

            elif user_input > get_random_number:
                print('Try Again! You guessed too high:' , user_input)

            else: 
                print(f'you get the answer in {number_repetiton} stops')
                print('ok, Congratulations!' 
                f'user input:{user_input} and random number:{get_random_number}')
                return
        else:      
            print('invalid input : the input should be number')

def create_random_number():

    while True:
        num_input1 = input('please enter your number 1: ')
        num_input2 = input('please enter your number 2: ')

        if num_input1.isdigit() and num_input2.isdigit():
            num_input1=int(num_input1)
            num_input2=int(num_input2)

            if num_input1 < num_input2:
                get_random_number = random.randint(num_input1,num_input2)
                print(f'optional random number: {get_random_number}') 
                select_user = get_user_input(num_input1 , num_input2 , get_random_number)
                return select_user
                

            print('the number2 most be biger of number1 ')
        else:
            print('invalid input : the input should be number')
def run():
    clear_screen()
    welcome_message_game_info()
    create_random_number()

run()