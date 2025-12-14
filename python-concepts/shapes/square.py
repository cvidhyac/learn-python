from .ashape import AShape

class Square(AShape):

    def __init__(self, side: float):

        if not Square.is_valid_side(side):
            raise ValueError("Invalid side provided")

        super().__init__("square")
        self.__side = side

    def area(self) -> float:
        return self.__side ** 2

    @staticmethod
    def is_valid_side(side: float) -> bool:
        return side > 1