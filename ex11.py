# Learning how to ask questions, can also use end=' '
# The computer will remember the input, then you can
#   use that input in another string, like line 11
print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()
# Here we can input the variable data we just collected
print(f"\nSo, you're {age} old, {height} tall, and {weight} heavy.")

# A little practice (limited to my current knowledge, lol)
print("""
Would you like:
\tPizza
\tBurger
\tSushi
""", end=" ")
order = input()

print("""
Would you like some toppings:
\tPepperoni
\tPineapple
\tKetchup
\tMustard
\tSoy Sauce
\tWasabi
""", end=" ")
toppings = input()

print(f"\nOkay, cool. So you want {order} with {toppings}.")
