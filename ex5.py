# Set variable values
name = 'Andy F. Cornelius'
age = 27
height_in = 73.00
height_cm = height_in * 2.54
weight_kg = 74.00
weight_lb = weight_kg * 2.20
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# Now, create the functions
print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"Which is {round(height_cm,2)} in centimeters.")
print(f"He's {weight_lb} pounds heavy.")
print(f"Which is {weight_kg} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}.")

# and then I guess we add them for fun?
total = age + height_in + weight_lb

print(f"If we add his age ({age}), his height in inches ({height_in}), and his weight in pounds ({weight_lb}), we get:", total)
