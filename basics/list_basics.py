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


if __name__ == '__main__':
    see_the_world()
    list_methods()
