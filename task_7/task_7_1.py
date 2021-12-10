class Rectangle:
    def __init__(self, side_a: float = 4, side_b: float = 3):
        if side_a <= 0 or side_b <= 0:
            raise ValueError
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side_a(self) -> float:
        """
        Return A side of the Rectangle.
        :return: side a of Rectangle
        :rtype: float
        """
        return self.__side_a

    def get_side_b(self) -> float:
        """
        Return B side of the Rectangle.
        :return: side b of Rectangle
        :rtype: float
        """
        return self.__side_b

    def area(self) -> float:
        """
        Calculate and return area of rectangle.
        :return: area of Rectangle
        :rtype: float
        """
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of Rectangle.
        :return: perimeter of Rectangle
        :rtype: float
        """
        return 2*(self.__side_a + self.__side_b)

    def is_square(self) -> bool:
        """
        Check if Rectangle is square.
        :return: True if rectangle is square, else False
        :rtype: bool
        """
        return self.__side_a == self.__side_b

    def replace_sides(self):
        """
        Swap sides of the Rectangle.
        """
        self.__side_a, self.__side_b = self.__side_b, self.__side_a

    def __str__(self):
        return f"Side A = {self.__side_a}, B = {self.__side_b}"


class ArrayRectangles:
    def __init__(self, *args, n: int = 0):
        rectangle_array = []
        if args:
            for element in args:
                if isinstance(element, Rectangle):
                    rectangle_array.append(element)
                else:
                    rectangle_array.extend(element)
        if len(rectangle_array) < n:
            for _ in range(n - len(rectangle_array)):
                rectangle_array.append(None)
        self.__rectangle_array = rectangle_array

    def add_rectangle(self, rectangle_to_add: Rectangle) -> bool:
        """
        Add rectangle of type Rectangle to the array on the nearest free place and return True, else return False.
        :param rectangle_to_add: rectangle to insert into rectangle array
        :type rectangle_to_add: Rectangle
        :return: Return
        :rtype: bool
        """
        if None in self.__rectangle_array:
            self.__rectangle_array[self.__rectangle_array.index(None)] = rectangle_to_add
        return False

    def number_max_area(self) -> int:
        """
        Returns index of the first rectangle with the largest area.
        :return: index of the first rectangle with largest area
        :rtype: int
        """
        max_area, max_area_index = 0, 0
        for index, item in enumerate(self.__rectangle_array):
            if item is not None and item.area() > max_area:
                max_area, max_area_index = item.area(), index
        return max_area_index

    def number_min_perimeter(self) -> int:
        """
        Return index of the first rectangle with the smallest perimeter.
        :return: index of the first rectangle with the smallest perimeter
        :rtype: int
        """
        min_perimeter, min_perimeter_index = float('inf'), 0
        for index, item in enumerate(self.__rectangle_array):
            if item is not None and item.perimeter() < min_perimeter:
                min_perimeter, min_perimeter_index = item.perimeter(), index
        return min_perimeter_index

    def number_of_squares(self) -> int:
        """
        Count number of squares in the array of rectangles
        :return: Number of squares in the array of rectangles
        :rtype: int
        """
        squares_count = 0
        for item in self.__rectangle_array:
            if item is not None and item.is_square():
                squares_count += 1
        return squares_count

    def __str__(self):
        return str(self.__rectangle_array)


# rect_default = Rectangle()
# rect_3x3 = Rectangle(3, 3)
# rect_2x4 = Rectangle(2, 4)
# rect_4x5 = Rectangle(4, 5)
# rect_4x4 = Rectangle(4, 4)
# rect_5x5 = Rectangle(5, 5)
#
# array_of_rectangles = ArrayRectangles(rect_default, [rect_3x3, rect_2x4, rect_4x5], rect_4x4, n=7)
# array_of_rectangles.add_rectangle(rect_5x5)
# print(array_of_rectangles.number_of_squares())
