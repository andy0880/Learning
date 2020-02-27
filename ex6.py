# Let's define variables
types_of_people = 10
x = f"There are {types_of_people} types of people."
# Two strings were placed inside of y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
# The strings were printed here. But why convert them to strings?
# I think, because that way it's easier to write them again, and again.
print(x)
print(y)
# It would have been very tedious to write them out again here.
# Also, x and y are two more strings placed inside a string.
print(f"I said: {x}")
print(f"I also said: '{y}'")
# This is the new lesson:
# Creating joke_evaluation allows us to use that sentence more than once.
# Then, we can input variables into a string with {} followed by .format()
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# When turned into variables, strings can be combines like any other function.
w = "This is the left side of..."
e = "a string with a right side."
# Is this technically another string in a string? Nah.
print (w + e)
