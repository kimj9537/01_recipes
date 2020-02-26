# To Do

# Ask user for servings made by recipe (and check this is a number that is more th
# Ask user for servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than 0.25 or more than 4

# Functions go here

# Number Checking Function
def num_check(question):



# Main Routine goes here

serving_size = float(input(" What is the recipe serving size? "))
desired_size = float(input(" How many servings are needed? "))

scale_factor = desired_size / serving_size

print("Scale Factor: {}".format(scale_factor))