def print_christmas_tree():
    row_count = int(input("Enter rows: "))
    for i in range(row_count):
        print(("*" * (2 * i + 1)).center(row_count * 2 - 1))
    output = ("*".center(row_count * 2 - 1))
    return output


print(print_christmas_tree())
