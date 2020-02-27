# We have 100 cars available
cars = 100
# Each car can seat 4 passengers
space_in_car = 4.0
# How many drivers are there?
drivers = 30
# How many passengers are there?
passengers = 90
# Cars without drivers
cars_not_driven = cars - drivers
# Cars with drivers
cars_driven = drivers
# How many seats are available in the cars driven?
carpool_capacity = cars_driven * space_in_car
# Pretty self-explanatory
average_passengers_per_car = passengers / cars_driven
# I guess this would be for a car service's capacity?

# Once variables are set, introduce functions
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
