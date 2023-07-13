import random
import string
import secrets


def randomStringGeneration(length: int, choice: int):
    """ Returns a random generated string based on the given choice and given length.
    
    Parameters
    ------------
        length: int
            The length of the string as required.
        choice: int
            The choice(listed below in Description) of string generation required.
            
    Return
    -----------
        randomString : string
            The desired random string type generated for use.
            
    Description
    ------------
        Following is a list of choices that are avaiable to generate random string of given length:
        
            1. Lowercase alphabets        
            2. Uppercase alphabets
            3. Mixed alphabets
            4. Lowercase with Numbers
            5. Uppercase with Numbers
            6. Mixed alphabets with Numbers
            7. Numbers(0-9)
            8. Mixed alphabets with Digits and Punctuations
            9. Hexadecimal number"""

    try:
        randomString = ''
        choice=int(choice)
        if (choice == 1):
            randomString = ''.join(random.choices(
                string.ascii_lowercase, k=length))
        elif (choice == 2):
            randomString = ''.join(random.choices(
                string.ascii_uppercase, k=length))
        elif (choice == 3):
            randomString = ''.join(random.choices(
                string.ascii_letters, k=length))
        elif (choice == 4):
            randomString = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=length))
        elif (choice == 5):
            randomString = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=length))
        elif (choice == 6):
            randomString = ''.join(random.choices(
                string.ascii_letters + string.digits, k=length))
        elif (choice == 7):
            randomString = ''.join(random.choices(string.digits, k=length))
        elif (choice == 8):
            randomString = ''.join(random.choices(
                string.ascii_letters + string.digits + string.punctuation, k=length))
        elif (choice == 9):
            randomString = ''.join(secrets.token_hex(length//2))
        else:
            randomString = "Option does not match to any of the predefined structure. Legitimate choices are from 1, 2, 3, 4, 5, 6, 7, 8 or 9."
        return randomString
    except:
        return "Invalid Parameter(s). The parameter(s) must be positive integers with second one being in range {1, 9}."
