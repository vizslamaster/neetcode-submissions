def add_two_numbers() -> int:
    my_input = input()
    my_list = [int(x) for x in my_input.split(",")]
    return my_list[0] + my_list[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
