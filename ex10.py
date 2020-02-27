# Define variables
# \t (backslash t) tabs the string
tabby_cat = "\tI'm tabbed in."
# \n (backslash n) moves string to the next line
persian_cat = "I'm split\non a line."
# \\ (double backslash) actually prints a \ character
backslash_cat = "I'm \\ a \\ cat."
# Here we use both """ (triple double-quotes) to print on
#   multiple lines, and \t to tab the list items.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# And then run the functions
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Let's try random Escape Sequences to see what they do:
# Still not sure what \a (bell) is supposed to do
print("What does \ado?")
# \b (backspace) is pretty straighforward, it's a backspace
print("What does \bdo?")
# Formfeed, kind of just did: \n + \t , if that makes sense
print("What does \fdo?")
# Carriage Return, it deleted "What" and replaced it with "do?"
print("What does \rdo?")
# Did the same as Formfeed, \n + \t
# I'm not saying that's what these two do, just what happened.
print("What does \vdo?")
# And of course, just made a space here for the final line.
print("\nThat's about all we'll try here.")

print('''
I'm not sure why I would use these ('').
It seems like these just do the same as """
Oh, but I guess if I want to write a tutorial
and use """, then I would need the '' instead.
It's also easier to write, I suppose (no Shift needed).
''')
