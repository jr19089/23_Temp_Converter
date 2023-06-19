def valid_check(choice, options):
    chosen = ""

    for var_list in options:

        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        return "invalid choice"


valid_words = [
    ["fahrenheit", "f"],
    ["celsius", "c"]
]


def check_temp(min_value):
    error = "Please enter a value higher than {}".format(min_value)
    error2 = "Please actually enter a number"

    valid = False
    while not valid:
        try:
            response = float(input("Please enter a number: "))

            if response < min_value:
                print(error)
            elif response == "":
                print(error2)
            else:
                valid = True
                return response

        except ValueError:
            print(error2)


def to_celsius(to_convert):
    answer = (to_convert - 32) * 5/9
    return answer


def to_fahrenheit(to_convert):
    answer = (to_convert * 9/5) + 32
    return answer


invalid = "invalid choice"
while invalid:
    choices = input("Convert to Celsius(C) or Fahrenheit(F)? ").lower()
    valid_choices = valid_check(choices, valid_words)

    if valid_choices == "Celsius":
        print("Converting to Celsius")
        degrees_f = check_temp(-459)
        converted = to_celsius(degrees_f)
        print(converted)
    elif valid_choices == "Fahrenheit":
        print("Converting to Fahrenheit")
        degrees_c = check_temp(-273)
        converted = to_fahrenheit(degrees_c)
        print(converted)
