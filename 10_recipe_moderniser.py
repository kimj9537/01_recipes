# modules to be used...
import csv
import re

# ***** Functions *****

def not_blank(question, error_msg, num_ok ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's number, complain
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Number checking function (number must be a float that is more than 0)
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print (error)

def get_sf():
    serving_size = num_check("What is the recipe serving size?" )

    # Main Routine goes here
    dodgy_sf = "yes"
    while dodgy_sf == "yes":


        desired_size = num_check(" How many servings are needed? ")

        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small "
                      "and you might struggle to accurately weigh "
                      "the ingredients. \n"
                      "Do you want to fix this and make more servings? ").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might"
                      "have issues with mixing bowl space / oven space. \n"
                      "Do you want to fix this and make a smaller batch? ").lower()
        else:
            dodgy_sf = "no"

    return scale_factor

def get_all_ingredients():
    all_ingredients = []

    stop =""
    print("Please enter ingredients one line at a time. Press 'xxx' to when"
          "you are done.")
    while stop != "xxx":
        # Ask user for ingredient (via not blank function)
        get_recipe_line = not_blank("Recipe Line: ",
                                   "This can't be blank",
                                   "yes")

        # Stop looping if exit code is typed and there are more
        # than 2 ingredients...
        if get_recipe_line.lower()== "xxx" and len(all_ingredients) > 1:
            break

        elif get_recipe_line.lower() == "xxx" and len(all_ingredients) <2:
            print("You need at least two ingredients in the list."
                  "Please add more ingredients.")

        # If exit code is not entered, add ingredient to list
        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients

def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]

def unit_checker(raw_unit):

    unit_tocheck = raw_unit

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t" "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp" "tablespoons"]
    ounce = ["oz", "fluid", "ounce", "fl", "oz", "ounces"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    mls = ["ml", "milliliter", "millilitre", "mL", "mililiters", "mililitres"]
    litre = ["liter", "litre", "L", "l", "litres", "liters"]
    dl = ["deciliter", "decilitre", "dL"]
    pound = ["pound", "lb", "#", "pounds"]
    grams = ["g", "gram", "grams"]


    if unit_tocheck == "":
       # print("you chose {}".format(unit_tocheck))
       return unit_tocheck
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "ml"
    elif unit_tocheck.lower() in litre:
        return "l"
    elif unit_tocheck.lower() in dl:
        return "dl"
    elif unit_tocheck.lower() in pound:
        return "pound"
    elif unit_checker.lower() in grams:
        return "g"

# ****** Main Routine Goes Here ********

# dictionaries go here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "mls": 1
}

# *** Generate food dictionary *****
# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# print(food_dictionary)


# Function to get (and check amount, unit and ingredient)



# ***** Main Routine *****

# set up Dictionaries

# ser up list to hold 'modernised' ingredients
modernised_recipe = []

# Ask user for recipe name and check its not blank
recipe_name = not_blank(" What is the recipe name? ",
                   "The recipe name can't be blank and can't contain numbers,",
                   "no")
# Ask user where the recipe is originally from (numbers OK)
source = not_blank(" Where is the recipe from? ",
                   "The recipe source can't be blank,",
                   "yes")


# Get serving sizes and scale factor
scale_factor = get_sf()

# Get amounts, units and ingredients from user...
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient...

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # Get amount...
    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)
        amount = amount * scale_factor

        # Get unit and ingredient...
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip() # remove extra white space from unit

    else:
        get_amount = recipe_line.split(" ", 1) # split line at first space

        try:
            amount = eval(get_amount[0]) # convert amount to float if possible
            amount = amount * scale_factor
        except NameError:
            amount = (get_amount[0])
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)    # splits text at first space

    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        # Item has unit and ingredient
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit =unit_checker(unit)
        # convert into ml

        # if unit is already in grams, add it to list
        if unit == "g":
            modernised_recipe.append("{:.0f} g {}".format(amount, ingredient))
            continue

        # convert to mls if possible...
        amount = general_converter(amount, unit, unit_central, 1)

        # if we converted to mls, try any convert to grams
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # if the ingredient is in the list, convert it
        if amount_2[1] == "yes":
            modernised_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient))   # Rather than printing, update modernised list (g)

        # if the ingredient in not in the list, leave the unit as ml
        else:
            modernised_recipe.append("{:.0f} ml {}".format(amount[0], ingredient))


    else:
        modernised_recipe.append("{} {}".format(amount, unit_ingredient))
        continue

    # modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))

# Put updated ingredient in list

# Output ingredient list
for item in modernised_recipe:
    print(item)
