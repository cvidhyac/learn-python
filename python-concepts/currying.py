"""
In functional programming, functions are broken down to pieces and conditionally invoked
clarifying intent better on what gets executed. This technique is called 'currying'
"""


def area_of_shape(name_of_the_shape: str):
    def area_of_square(side: int) -> float:
        return side ** 2

    def area_of_circle(radius: int) -> float:
        return 3.14 * radius ** 2

    def area_of_rectangle(length: int, breadth: int) -> float:
        return length * breadth

    if name_of_the_shape == 'square':
        return area_of_square
    elif name_of_the_shape == 'circle':
        return area_of_circle
    elif name_of_the_shape == 'rectangle':
        return area_of_rectangle
    else:
        raise ValueError(f"Invalid shape '{name_of_the_shape}'")


if __name__ == '__main__':
    sq_area = area_of_shape(name_of_the_shape='square', )(3)
    circle_area = area_of_shape(name_of_the_shape='circle', )(4)
    rectangle_area = area_of_shape(name_of_the_shape='rectangle', )(5, 6)
    print(f"The area of square: {sq_area}, circle area: {circle_area}, rectangle area: {rectangle_area}")
