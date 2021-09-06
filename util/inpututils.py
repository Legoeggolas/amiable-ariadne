from typing import Any


# Utility function
# Takes type validated input
def take_input(input_type, msg="", scope=[]) -> Any:
    temp = None
    while type(temp) != input_type:
        temp = input(msg)

        try:
            temp = input_type(temp)
        except:
            print("Your input type is incorrect")
            temp = None

        if input_type == str:
            temp = temp.lower()

        if scope and temp not in scope:
            print("Your input does not match anything in the scope")
            temp = None

    return temp