"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)  # printing empty list
my_numbers.append(1.5)  # adding to the list
my_numbers.append(2.5)
print(my_numbers)

# create an already populated lists
game_points: list[int] = [102, 86, 94]
print(game_points)

# print(game_points[2]) #printing out one of the data points

game_points[1] = 72  # modifying info to different data
print(game_points)

# Getting length of lists
print(len(game_points))

# Removing item from list
game_points.pop(1)
print(game_points)


def display(input: list[int]) -> None:
    idx: int = 0
    while idx < len(input):
        print(input[idx])
        idx += 1


display(input=game_points)
