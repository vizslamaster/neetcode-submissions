from typing import List

def read_integers() -> List[int]:
    my_input = input()
    my_list = [int(x) for x in my_input.split(",")]
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
