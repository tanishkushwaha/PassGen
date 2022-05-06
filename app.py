import random
import string
from tkinter import *

def genPass(passLen, passConfig):

    if passLen == '':
        result.configure(text='Invalid Length!')
        return

    symbols = '!@#$%^&*()'
    characters = ''

    if '1' in passConfig:
        symFlag = True
        characters += symbols

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
    for _ in range (int(passLen)):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    return ''.join(password)

def generateButton():
    flagString = str(var1.get()) + "" + str(var2.get()) + "" + str(var3.get()) + "" + str(var4.get())
    p = genPass(textBox1.get(), flagString)
    result.configure(text=p)

master = Tk()
master.title('PassGen')

Label(master, text='Password Length:').grid(row=0, column=0, sticky='w')
textBox1 = Entry(master)
textBox1.grid(row=0, column=1)

var1 = IntVar()
Checkbutton(master, text='Symbols', variable=var1, onvalue=1).grid(row=1, column=0, sticky='w')

var2 = IntVar()
Checkbutton(master, text='Numbers', variable=var2, onvalue=2).grid(row=2, column=0, sticky='w')

var3 = IntVar()
Checkbutton(master, text='Lowercase Characters', variable=var3, onvalue=3).grid(row=3, column=0, sticky='w')

var4 = IntVar()
Checkbutton(master, text='Uppercase Characters', variable=var4, onvalue=4).grid(row=4, column=0, sticky='w')

Button(master, text='Generate', command=generateButton).grid(row=5, column=0, sticky='w')

result = Label(master, text='Your Password')
result.grid(row=5, column=1)

mainloop()

