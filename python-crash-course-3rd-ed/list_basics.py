def see_the_world():
    locations = ['Toronto', 'Delhi', 'Dubai', 'Sydney', 'Shanghai']
    print(f"The original list of locations: {locations}")
    sorted_list = sorted(locations)
    print(f" The sorted list - {sorted_list}")
    sorted_list.reverse()
    print(f"The reversed list {sorted_list}")
    another_locations = locations
    another_locations.sort()
    print(f"List copied over to - {another_locations}")
    another_locations.sort(reverse=True)
    print(f"Another locations reversed - {another_locations}")
    print(f"Check on original locations again {locations}")
    print(f"check list size - {len(locations)}")

def list_methods():
    example_list = ["Apple", "Banana", "Cherry", "Grapes", "Oranges"]
    print(f"The original list {example_list}")
    example_list.append("Strawberries")
    print(f"After adding another fruit - {example_list}")
    example_list.insert(1, 'Kiwi')
    print(f"After inserting a fruit in index[1] {example_list}")
    print(f"Print second element in fruit list - {example_list[1]}")
    print(f"Print last but second element from list - {example_list[-2]}")
    del example_list[0]
    print(f"Delete Element at index 0 using del keyword - {example_list}")
    print(f"Pop the last element in the list = {example_list.pop()}")
    print(f"Pop an element from specific position index 2 - {example_list.pop(2)}")
    example_list.remove('Grapes')
    print(f"Remove by value 'grapes' - {example_list}")


def list_slicing():
    nums = [num for num in range(1, 100_000)]
    subset_of_ten_nums = nums[0:10]
    print(f"Subset of first ten nums - {subset_of_ten_nums}")
    subset_of_20_30_nums = nums[19:30]
    print(f"subset of next ten nums form 20 to 30 indexes - {subset_of_20_30_nums}")
    subset_of_rest = nums[99_000:]
    print(f"Everything after index 99,000: {subset_of_rest}")
    subset_of_first_fifty = nums[:50]
    print(f"First fifty: {subset_of_first_fifty}")

def shallow_copy_a_list():
    list_of_nums = [num for num in range(0, 10)]
    a_copy_of_list = list_of_nums[:]
    a_copy_of_list.append(10)
    print(f"Original ist {list_of_nums}")
    print(f"a copy of the list with additional number - {a_copy_of_list}")

def search_elements():
    toppings = ["Mushroom", "Onion", "Pineapple", "Tomato", "Olives"]
    requested_toppings = ["French Fries", "Mushroom"]
    if toppings:
        for topping in requested_toppings:
            if topping in toppings:
                print(f"the toppings {topping} is available, adding to pizza " )
            else:
                print(f"The topping {topping} is not available, choose another one")


if __name__ == '__main__':
    see_the_world()
    list_methods()
    list_slicing()
    shallow_copy_a_list()
    search_elements()
