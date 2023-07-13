import random
import string

def randomStringGeneration(length, choice):
    #1. lowercase alphabets
    #2. uppercase alphabets
    #3. mixed alphabets
    #4. lowercase with numbers
    #5. uppercase with numbers
    #6. mixed alphabets with numbers
    #7. numbers(0-9)
    randomString=''
    if(choice==1):
        randomString = ''.join(random.choices(string.ascii_lowercase, k=length))
    elif(choice==2):
        randomString = ''.join(random.choices(string.ascii_uppercase, k=length))
    elif(choice==3):
        randomString = ''.join(random.choices(string.ascii_letters, k=length))
    elif(choice==4):
        randomString = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    elif(choice==5):
        randomString = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    elif(choice==6):
        randomString = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif(choice==7):
        randomString = ''.join(random.choices(string.digits, k=length))
    elif(choice==8):
        randomString = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    else:
        randomString="Option does not match to any of the predefined structure. Legitimate choices are from 1, 2, 3, 4, 5, 6, 7 or 8"
    return randomString
