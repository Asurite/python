# Using Webbrowser, re, and one other module give me a useful code that I can use in one of my projects

# Here's a Python code that takes you to a random website.

import webbrowser
import re
import random

websites = ['https://www.google.com', 'https://www.twitter.com' 'https://www.youtube.com', 'https://www.github.com']
chosen_website = random.choice(websites) # Randomly choose a website from the list
webbrowser.open_new_tab(chosen_website) # Open the website in a new tab using webbrowser

# Extract the domain name from the URL using regular expressions and print it
domain_name = re.findall('(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)', chosen_website)
print("Welcome aboard, we're  travelling to:", domain_name[0])
