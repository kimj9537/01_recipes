# **** Get items etc *****

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary.
    unit = unit_checker()
    ingredient = input("Ingredient: ")

    # Convert to mls if possible
    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    # If we converted to mls, try and convert to grams
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # if the ingredient is in the list, convert it
        if amount_2[1] == "yes":
            print(amount_2)

        # if the ingredient is not in the list, leave the unit as ml
        else: print("unchanged")

    # If the unit is not mls, leave the line unchanged
    else:
        print("unchanged")

    # keep_going = input("<enter> or q ")



















