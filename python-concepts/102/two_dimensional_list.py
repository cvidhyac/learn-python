def demo_two_dimensional_list():
    vals = [[45, 56, 67], [34, 45, 56], [67, 78, 89]]
    for i, row in enumerate(vals):
        for j, col in enumerate(row):
            print(f"The value of matrix element a [{i}][{j}] is {col}")

    # find average by using formula total / no. of items
    total = 0
    no_of_items = 0
    for i, row in enumerate(vals):
        total += sum(row)
        no_of_items += len(row)
        print(f"The sum of each row {i} is {sum(row)}, and row Length is {len(row)}")

    average = total / no_of_items
    print(f"The average value of each row is {average}")


if __name__ == '__main__':
    demo_two_dimensional_list()