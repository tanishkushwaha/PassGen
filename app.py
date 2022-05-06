import random
import string
from tkinter import *


def genPass(passLen, passConfig):

    characters = ''

    if '1' in passConfig:
        symFlag = True
        characters += string.punctuation

    if '2' in passConfig:
        numFlag = True
        characters += string.digits

    if '3' in passConfig:
        lowCharFlag = True
        characters += string.ascii_lowercase

    if '4' in passConfig:
        upCharFlag = True
        characters += string.ascii_uppercase

    characters = list(characters)
    random.shuffle(characters)

    password = []
    for _ in range (passLen):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    return ''.join(password)



master = Tk()
master.title('PassGen')

Label(master, text='Password Length:').grid(row=0, column=0, sticky='w')
textBox1 = Entry(master).grid(row=0, column=2)

var1 = IntVar()
Checkbutton(master, text='Symbols', variable=var1).grid(row=1, column=0, sticky='w')

var2 = IntVar()
Checkbutton(master, text='Numbers', variable=var2).grid(row=2, column=0, sticky='w')

var3 = IntVar()
Checkbutton(master, text='Lowercase Characters', variable=var3).grid(row=3, column=0, sticky='w')

var4 = IntVar()
Checkbutton(master, text='Uppercase Characters', variable=var4).grid(row=4, column=0, sticky='w')

Label(master, text='Your Password').grid(row=5, columnspan=3)


mainloop()

