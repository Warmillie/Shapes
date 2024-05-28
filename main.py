import math
from abc import ABC, abstractmethod
import enum 

class Shape(ABC):
    @abstractmethod
    def perimeter(self) -> float | None:
        pass
    @abstractmethod
    def area(self) -> float | None:
        pass

class Parts:

    def __init__(self, parts: list[str]):
        self.__parts = parts
        self.__parts_dict = dict()

    def parsed_parts(self) -> dict[str]:
        _last_part_name: str = None

        for part in self.__parts:
            try:
                value_to_insert = float(part)
                self.__parts_dict[_last_part_name].append(value_to_insert)
            except ValueError:
                _last_part_name = part
                self.__parts_dict[_last_part_name] = []
        return self.__parts_dict

class ShapeTypes(enum.Enum):
    SQUARE = 'square'
    RECTANGLE = 'rectangle'
    CIRCLE = 'circle'
    TRIANGLE = 'triangle'

    @classmethod
    def get_shape_type(cls, shape_type: str):
        if shape_type == 'square':
            return ShapeTypes.SQUARE
        elif shape_type == 'rectangle':
            return ShapeTypes.RECTANGLE
        elif shape_type == 'circle':
            return ShapeTypes.CIRCLE
        elif shape_type == 'triangle':
            return ShapeTypes.TRIANGLE
class Square(Shape):
    def __init__(self, parts_dict: dict):
        self._parts: dict = parts_dict
        self.side = None

        self._convert_values()

    def _convert_values(self):
        side: list[float] = self._parts['Side'] if "Side" in self._parts else None
        if side is not None:
            self.side = side[0]
        else:
            if 'TopLeft' in self._parts and 'BottomLeft' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                self.side = math.sqrt((bottom_left_x - top_left_x) ** 2 + (bottom_left_y - top_left_y) ** 2)
            elif 'BottomLeft' in self._parts and 'BottomRight' in self._parts:
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                self.side = math.sqrt((bottom_left_x - bottom_right_x) ** 2 + (bottom_left_y - bottom_right_y) ** 2)
            elif 'BottomRight' in self._parts and 'TopRight' in self._parts:
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                top_right_x, top_right_y = self._parts['BottomRight']
                self.side = math.sqrt((top_right_x - bottom_right_x) ** 2 + (bottom_right_y - top_right_y) ** 2)
            elif 'TopRight' in self._parts and 'TopLeft' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                top_right_x, top_right_y = self._parts['BottomRight']
                self.side = math.sqrt((top_right_x - top_left_x) ** 2 + (top_left_y - top_left_x) ** 2)
            elif 'TopLeft' in self._parts and 'BottomRight' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                self.side_w = abs(bottom_right_x - top_left_x)
                self.side_h = abs(top_left_y - bottom_right_y)
            elif 'TopRight' in self._parts and 'BottomLeft' in self._parts:
                top_right_x, top_right_y = self._parts['TopRight']
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                self.side_w = abs(top_right_x - bottom_left_x)
                self.side_h = abs(top_right_y - bottom_left_y)
            else:
                raise ValueError("Either side length or coordinates should be provided for Square")

    def perimeter(self) -> float | None:
        if self.side is not None:
            return 4 * self.side
        else:
            raise ValueError("Either side length or coordinates should be provided for Square")

    def area(self) -> float | None:
        if self.side is not None:
            return self.side ** 2
        else:
            raise ValueError("Either side length or coordinates should be provided for Square")

class Rectangle(Shape):
    def __init__(self, parts_dict: dict):
        self._parts = parts_dict
        self.side_w = None
        self.side_h = None



        self._convert_values()
    def _convert_values(self):
        side: list[float] = self._parts['Side'] if "Side" in self._parts else None
        if side is not None:
            self.side_w = side[0]
            self.side_h = side[1]

        else:

            if 'TopLeft' in self._parts and 'BottomLeft' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                self.side_w = math.sqrt((bottom_left_x - top_left_x) ** 2 + (bottom_left_y - top_left_y) ** 2)
            elif 'BottomLeft' in self._parts and 'BottomRight' in self._parts:
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                self.side_h = math.sqrt((bottom_left_x - bottom_right_x) ** 2 + (bottom_left_y - bottom_right_y) ** 2)
            elif 'BottomRight' in self._parts and 'TopRight' in self._parts:
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                top_right_x, top_right_y = self._parts['TopRight']
                self.side_w = math.sqrt((top_right_x - bottom_right_x) ** 2 + (bottom_right_y - top_right_y) ** 2)
            elif 'TopRight' in self._parts and 'TopLeft' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                top_right_x, top_right_y = self._parts['TopRight']
                self.side_h = math.sqrt((top_right_x - top_left_x) ** 2 + (top_left_y - top_left_x) ** 2)
            elif 'TopLeft' in self._parts and 'BottomRight' in self._parts:
                top_left_x, top_left_y = self._parts['TopLeft']
                bottom_right_x, bottom_right_y = self._parts['BottomRight']
                self.side_w = abs(bottom_right_x - top_left_x)
                self.side_h = abs(top_left_y - bottom_right_y)
            elif 'TopRight' in self._parts and 'BottomLeft' in self._parts:
                top_right_x, top_right_y = self._parts['TopRight']
                bottom_left_x, bottom_left_y = self._parts['BottomLeft']
                self.side_w = abs(top_right_x - bottom_left_x)
                self.side_h = abs(top_right_y - bottom_left_y)
            else:
                raise ValueError("Either side length or coordinates should be provided for Square")

    def perimeter(self) -> float | None:
        print(self.side_w, self.side_h)
        if self.side_w is not None and self.side_h is not None:
            return 2 * (self.side_w + self.side_h)
        else:
            raise ValueError("Either side length or coordinates should be provided for Rectangle")

    def area(self) -> float | None :
        if self.side_w is not None and self.side_h is not None:
            return self.side_w * self.side_h
        else:
            raise ValueError("Either side length or coordinates should be provided for Rectangle")


class Circle(Shape):
    def __init__(self, parts_dict: dict):
        self._parts = parts_dict
        self.center_x = None
        self.center_y = None
        self.radius = None

        self._convert_values()

    def _convert_values(self):
        if 'Center' not in self._parts or 'Radius' not in self._parts:
            raise ValueError("Center coordinates and radius should be provided for Circle")

        self.center_x, self.center_y = self._parts['Center']
        self.radius = self._parts['Radius']

    def perimeter(self):
        if self.radius is None:
            raise ValueError("Radius should be provided for Circle")
        else:
            return 2 * math.pi * self.radius

    def area(self):
        if self.radius is None:
            raise ValueError("Radius should be provided for Circle")
        else:
            return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, parts_dict: dict):
        self._parts = parts_dict
        self.side_a = None
        self.side_b = None
        self.side_c = None

        self._convert_values()

    def _convert_values(self):
        if 'Point1' in self._parts and 'Point2' in self._parts and 'Point3' in self._parts:
            point1_x, point1_y = self._parts['Point1']
            point2_x, point2_y = self._parts['Point2']
            point3_x, point3_y = self._parts['Point3']
            self.side_a = math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)
            self.side_b = math.sqrt((point3_x - point2_x) ** 2 + (point3_y - point2_y) ** 2)
            self.side_c = math.sqrt((point1_x - point3_x) ** 2 + (point1_y - point3_y) ** 2)
        else:
            raise ValueError("Coordinates of all three points should be provided for Triangle")

    def perimeter(self) -> float | None:
        if self.side_a is not None and self.side_b is not None and self.side_c is not None:
            return self.side_a + self.side_b + self.side_c
        else:
            raise ValueError("Either side lengths or coordinates should be provided for Triangle")

    def area(self) -> float | None:
        if self.side_a is not None and self.side_b is not None and self.side_c is not None:
            s = (self.side_a + self.side_b + self.side_c) / 2
            return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        else:
            raise ValueError("Either side lengths or coordinates should be provided for Triangle")

class IzolesesTriangle(Triangle):
    def __init__(self, parts_dict: dict):
        super().__init__({'Point1': [0, 0], 'Point2': [0, 0], 'Point3': [0, 0]})
        self._parts = parts_dict
        self.side_a = None
        self.side_b = None
        self.side_c = None

        self._convert_values()
    def _convert_values(self):
        side: float = self._parts['Side'] if "Side" in self._parts else None
        if side is not None:
            self.side_a = side 
            self.side_b = side 
            self.side_c = side 


def main(input_string):
    line = input_string.strip().split('\n')[0]
    parts = line.split()
    shape_type = parts.pop(0).lower()
    shape = ShapeTypes.get_shape_type(shape_type)
    parts_parser = Parts(parts).parsed_parts()
    print(parts_parser)
    output = []

    if shape == ShapeTypes.SQUARE:
        fig = Square(parts_parser)
    elif shape == ShapeTypes.RECTANGLE:
        fig = Rectangle(parts_parser)
    elif shape == ShapeTypes.CIRCLE:
        fig = Circle(parts_parser)
    elif shape == ShapeTypes.TRIANGLE:
        fig = Triangle(parts_parser)
    else:
        raise ValueError("Shape type not supported")
    shape_type = type(shape).__name__
    perimeter = fig.perimeter()
    area = fig.area()
    output.append(f"{shape_type} Perimeter {perimeter:.2f} Area {area:.2f}")

    return "\n".join(output)


if __name__ == '__main__':
    while True:
        input_string = input('Input data (or type "exit" to quit): ')
        if input_string.lower() == 'exit':
            break
        print(main(input_string))
