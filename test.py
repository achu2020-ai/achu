def print_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)
    # trunk
    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "*" + trunk_spaces)

print_christmas_tree(10)