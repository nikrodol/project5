""" Упрощенная модель книжного шифра
    (используется одна страница).
"""
import random

def book_cipher (crypto_key, your_textfile, encrypting_text text=[]):
    with open(crypto_key) as f_in:
        try:
            text=f_in.readlines()
        except:
            print('Oh Fuck!')
    with open(encrypting_text) as f_out:
        text2=f_out.read()
    with open(encrypting_text, 'a+') as f_out:
        crypto_text=''
        i=0
        random_number=random.randint(1, len(text))
        random_line=text[random_number-1]#Рандомная строчка
        print(type(text[random_number-1]))
        for k in text2: #Шифруем по буквам
            print(len(text2), len(text))
            while random_line.find(text2[i]) == -1:
                random_number=random.randint(1, len(text))
                random_line=text[random_number-1]
            print(str(random_number) + ':' + str(random_line.find(text2[i])))
            crypto_text+=str(random_number) + ':' + str(random_line.find(text2[i])+1) + ' '
            i+=1
            print(crypto_text)
            random_number = random.randint(1, len(text))
            random_line = text[random_number - 1]
        f_out.write('')




chosen_file01 = input('Enter name of file for crypto-key: ') #Only "input.txt" use in repository
chosen_file02 = input('Enter name of file for encrypting text: ')#Only "output.txt" use in repository
chosen_file03 = input('Enter name of file for encrypting text: ')
book_cipher(chosen_file01, chosen_file02)

