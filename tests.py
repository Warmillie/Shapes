import unittest
from main import Square, Rectangle, Circle, Triangle

class TestShapes(unittest.TestCase):

    def test_square_perimeter(self):
        square = Square({'TopRight': [1, 1], 'Side': [1]})
        self.assertAlmostEqual(square.perimeter(), 4, places=2)

    def test_square_area(self):
        square = Square({'TopRight': [1, 1], 'Side': [1]})
        self.assertAlmostEqual(square.area(), 1, places=2)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle({'TopRight': [2, 2], 'BottomLeft': [1, 1]})
        self.assertAlmostEqual(rectangle.perimeter(), 4, places=2)  # Corrected expected value

    def test_rectangle_area(self):
        rectangle = Rectangle({'TopRight': [2, 2], 'BottomLeft': [1, 1]})
        self.assertAlmostEqual(rectangle.area(), 1, places=2)

    def test_circle_perimeter(self):
        circle = Circle({'Center': [1, 1], 'Radius': 2})
        self.assertAlmostEqual(circle.perimeter(), 12.57, places=2)

    def test_circle_area(self):
        circle = Circle({'Center': [1, 1], 'Radius': 2})
        self.assertAlmostEqual(circle.area(), 12.57, places=2)

    def test_triangle_perimeter(self):
        triangle = Triangle({'Point1': [0, 0], 'Point2': [0, 3], 'Point3': [4, 0]})
        self.assertAlmostEqual(triangle.perimeter(), 12, places=2)

    def test_triangle_area(self):
        triangle = Triangle({'Point1': [0, 0], 'Point2': [0, 3], 'Point3': [4, 0]})
        self.assertAlmostEqual(triangle.area(), 6, places=2)

if __name__ == '__main__':
    unittest.main()
