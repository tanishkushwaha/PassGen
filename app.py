import random
import string

from numpy import character

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



passLen = int(input('Password Length: '))
print('1. Include Symbols \n2. Include Numbers \n3. Include Lowercase Characters\
    \n4. Include Uppercase Characters')

passConfig = input('Enter Flags (1-4): ')

print(f'Your Password: {genPass(passLen, passConfig)}')

