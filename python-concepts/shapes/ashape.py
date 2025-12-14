from abc import abstractmethod, ABC


class AShape(ABC):
    category = "Geometric Shapes"

    def __init__(self, shape_type):
        self._shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

    @property
    def shape_type(self):
        return self._shape_type
