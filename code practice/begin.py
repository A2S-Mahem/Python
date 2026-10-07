# print("Five is greater than two!")
# print("Hello, World!") 
# ctrl+/ for commenting
"""
This is a simple Python script that prints a joke.
For more jokes, you can install the 'pyjokes' library using pip:
pip install pyjokes

"""
import pyjokes
print(pyjokes.get_joke())
print('''
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
''')
import pyttsx3
pyttsx3.speak('''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
''')


import os

# Get the contents of the current directory
contents = os.listdir()

# Print the contents
print("Contents of the directory:")

for item in contents:
    print(item)
