# Define variable "formatter"
formatter = "{} {} {} {}"
# use the .format() function to make "formatter" a function?
# I'm really not too sure
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# So you format the format to put the format in the format.
print(formatter.format(formatter, formatter, formatter, formatter))
# I guess this line makes the most sense:
# because "formatter" would join the strings in one row.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
# Still a bit confusing but I think I get it.
# Perhaps I'm just reading way too much into it.
