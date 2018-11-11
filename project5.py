""" Упрощенная модель книжного шифра
    (используется одна страница).
"""
import random

def book_cipher (crypto_key, your_textfile, encrypting_text, text=[]):
    with open(crypto_key) as f_key:
        try:
            key_text=f_key.readlines()
        except:
            print('Oh Fuck!')
    with open(your_textfile) as f_in:
        your_text=f_in.read()
    with open(encrypting_text, 'w') as f_out:
        crypto_text=''
        i=0
        random_number=random.randint(1, len(key_text))
        random_line=key_text[random_number-1]#Рандомная строчка
        print(type(key_text[random_number-1]))
        for k in your_text: #Шифруем по буквам
            print(len(your_text), len(key_text))
            while random_line.find(text2[i]) == -1:
                random_number=random.randint(1, len(key_text))
                random_line=key_text[random_number-1]
            print(str(random_number) + ':' + str(random_line.find(text2[i])))
            crypto_text+=str(random_number) + ':' + str(random_line.find(text2[i])+1) + ' '
            i+=1
            print(crypto_text)
            random_number = random.randint(1, len(key_text))
            random_line = key_text[random_number - 1]
        f_out.write(crypto_text)


chosen_file01 = input('Enter name of file for crypto-key: ') #Only "key.txt" use in repository
chosen_file02 = input('Enter name of file with yout text: ')#Only "intput.txt" use in repository
chosen_file03 = input('Enter name of file for encrypting text: ')#Only "output.txt" use in repository
book_cipher(chosen_file01, chosen_file02, chosen_file03)