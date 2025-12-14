from shapes import square, circle


def demo_polymorphism():
    a_circles = [circle.Circle(radius=5), circle.Circle(radius=6), circle.Circle(radius=7)]
    a_squares = [square.Square(side=4), square.Square(side=7), square.Square(side=9)]
    a_combined_list = a_circles + a_squares
    for shape in a_combined_list:
        current_area = shape.area()  # Print area irrespective of type of shape without knowing its internals
        print(f"The area of the shape of type {shape.shape_type} is {current_area}, belongs to category {shape.category}")

    # Create circle from diameter instead of radius
    another_circle = circle.Circle.from_diameter(diameter=10)
    print(f"The radius of another_circle is {another_circle.get_radius()}")

if __name__ == '__main__':
    demo_polymorphism()
