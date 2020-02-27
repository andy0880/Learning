# A simple printed string
print("Mary had a little lamb.")
# I guess by putting .format(),
# we don't need to define the variable beforehand?
# Correction: 'snow' is actually not a variable, just a string.
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? Multiplied the "." 10 times?
# I'm guessing output will be ".........."

# Defining variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch the comma at the end. Try removing it to see what happens.
# It doesn't work if you remove it, won't understand it's a separate function.
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
print(end7 + end8 + end9 + end10 + end11 + end12)
