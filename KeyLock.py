from random import *
import os
################################################################
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = '1234567890'
psw_list = []
################################################################
def generator(le, c):
    psw = ''
    l = len(chars)
    for i in range(le):
        p = randrange(l)
        c = chars[p]
        psw += c
    return psw

def input_yes_no(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            break
        else:
            print('Please enter "y" or "n".')
    if user_input == 'y':
        variable_name = 'y'
    else:
        variable_name = 'n'
    return variable_name

def input_integer(prompt):
    while True:
        flag = True
        user_input = input(prompt).lower()
        for i in user_input:
            if i in '1234567890':
                pass
            else:
                print('Eror, enter a number!')
                flag = False
                break
        if flag:
            return int(user_input)
################################################################
print('''888 88P                   888                        888    
888 8P   ,e e,  Y8b Y888P 888      e88 88e   e88'888 888 ee 
888 K   d88 88b  Y8b Y8P  888     d888 888b d888  '8 888 P  
888 8b  888   ,   Y8b Y   888  ,d Y888 888P Y888   , 888 b  
888 88b  "YeeP"    888    888,d88  "88 88"   "88,e8' 888 8b 
                   888                                      
                   888''')
num = input_integer('Number of passwords: ')

length = input_integer('Password length: ') 

inc_upp = input_yes_no('Include upper letters "ABCDEFGHIJKLMNOPQRSTUVWXYZ" [Y/n] ')

inc_low = input_yes_no('Include lower letters "abcdefghijklmnopqrstuvwxyz" [Y/n] ')

inc_spec = input_yes_no('Include special characters "!#$%&*+-=?@^_?" [Y/n] ')

exc_duo = input_yes_no('Include two-digit characters? (il1Lo0O) [Y/n] ')

saving_to_a_txt_file = input_yes_no('Save passwords to a txt file [Y/n] ') 
################################################################
if inc_low.lower() == 'y':
    chars += lowercase_letters
if inc_upp.lower() == 'y':
    chars += uppercase_letters
if inc_spec.lower() == 'y':
    chars += punctuation
if exc_duo.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')
################################################################
for i in range(num):
    print(generator(length, chars))
    psw_list.append(generator(length, chars))
    
if saving_to_a_txt_file=='y':
    file_path = os.path.expanduser("~/Desktop/passwords.txt")
    with open(f'{file_path}passwords.txt', 'w') as f:
        f.write('\n'.join(map(str, psw_list)))
