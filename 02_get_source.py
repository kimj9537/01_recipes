# Get's source of recipe name and checks it it not blank

# To Do
# Allow users to specifiy a custom error message
# Allow uesrs to specify whether numbers are allowed


# Not Blank Function goes here
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


# Main Routine goes here

source = not_blank(" Where is the recipe from? ",
                   "The recipe source can't be blank,",
                   "yes")

print("The recipe is from {}".format(source))