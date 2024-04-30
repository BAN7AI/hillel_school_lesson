def first_input_user(one_value):
    while True:
        if one_value.isdigit():
            one_value = int(one_value)
            break
        elif one_value.replace('.', '').isdigit():
            one_value = float(one_value)
            break
        else:
            one_value = input("Please write value int or float here: ")
    return one_value


def second_input_user(two_value):
    while True:
        if two_value.isdigit():
            two_value = int(two_value)
            break
        elif two_value.replace(".", "").isdigit():
            two_value = float(two_value)
            break
        else:
            two_value = input("Please write value int or float here: ")
    return two_value


one_answer = first_input_user(input("Write your first value here: "))
two_answer = second_input_user(input("Write your second value here: "))
three_value = input("Write here action: ")

while True:
    if three_value == "*":
        print(f"Your answer = {one_answer + two_answer}")
        break
    elif three_value == "/":
        print(f"Your answer = {one_answer + two_answer}")
        break
    elif three_value == "+":
        print(f"Your answer = {one_answer + two_answer}")
        break
    elif three_value == "-":
        print(f"Your answer = {one_answer + two_answer}")
        break
    else:
        three_value = input("Please write correct action here: ")
