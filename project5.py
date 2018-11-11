""" Упрощенная модель книжного шифра
    (используется одна страница; используя базовый текст в файле-ключе
     допускаются некоторый набор знаков препинания и кириллические буквы, цифры не допускаются;
     в случае нужды введите более полный текст).
"""
from random import randint


def book_cipher(crypto_key, your_textfile, encrypting_text):
    try:
        with open(crypto_key) as f_key:  # Reading file with key-text
            key_text = f_key.readlines()
            print('Oh Fuck!')
        with open(your_textfile) as f_in:  # Reading file with your text
            your_text = f_in.read().lower()
        with open(encrypting_text, 'w') as f_out:
            crypto_text = ''  # Creation string-variable
            i = 0  # This iterator for running along number letter in line of your text.
            random_number = randint(1, len(key_text)) # Choise random number of line in key_text
            random_line = key_text[random_number-1]  # Choise line in key_text
            for char in your_text:  # Running along your text by letter-iterator
                while random_line.find(your_text[i]) == -1:  # Check presence letter in this line
                    random_number = randint(1, len(key_text))
                    random_line = key_text[random_number-1]
                # Creation crypto-text and сhange number of line and line
                crypto_text += str(random_number) + ':' + str(random_line.find(your_text[i])+1) + ' '
                i += 1
                random_number = randint(1, len(key_text))
                random_line = key_text[random_number - 1]
            f_out.write(crypto_text)
            print("Process finished and created crypto-text in the file '{}'".format(encrypting_text))
    except FileNotFoundError:
        print('We have problem with names of files. Please, enter names of files again.')
        choise_file()
    except:
        print('Sorry, we don\' know why this programm have problem. Please, check presence key-text in key-file'
              'May be run this programm again?')
        choise_file() if input('Your answer: ').lower() == 'yes' else print('Okey. Goodbye!')


def choise_file():
    chosen_file01 = input('Enter name of file for crypto-key: ')  # Only "key.txt" use in repository
    chosen_file02 = input('Enter name of file with yout text: ')  # Only "intput.txt" use in repository
    chosen_file03 = input('Enter name of file for encrypting text: ')  # Only "output.txt" use in repository
    book_cipher(chosen_file01, chosen_file02, chosen_file03)


choise_file()
