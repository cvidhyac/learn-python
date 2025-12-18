import math
from .ashape import AShape

class Circle(AShape):

    def __init__(self, radius:float):
        super().__init__("circle") # protected scope

        if not Circle.is_valid_radius(radius):
            raise ValueError(f"Invalid radius: {radius}")

        self.__radius = radius # private scope


    def area(self) -> float:
        return self.__radius * self.__radius * math.pi

    def get_radius(self) -> float:
        return self.__radius

    @classmethod
    def from_diameter(cls, diameter:float) -> Circle:
        return cls(radius=diameter/2)

    @staticmethod
    def is_valid_radius(radius: float) -> bool:
        return radius > 1
