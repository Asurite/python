import random # defines a series of functions for generating or manipulating random integers.
import string # we have to import it before using any of its constants and classes.
def function_one(length):
 characters = string.ascii_letters + string.digits + string.punctuation 
 # string.ascii_letters : a constant that returns ascii_lowercase and ascii_uppercase constants.
 # string.digits : a constant that returns the text string:'0123456789'.
 # string.punctuation : a constant that returns all punctuation characters.
 return ''.join(random.choice(characters) for _ in range(length))
 # "join" used to put together a random characters for len/length times.
 # "return" returns the result of the string.
 ## so we're basically putting together random charcters for a len of times from function_one and adding them to a variable called _