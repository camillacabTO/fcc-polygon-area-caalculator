from math import floor


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2* self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture = picture + f'{"*" * self.width}\n'
        return picture

    def get_amount_inside(self, shape):
        width_amount = self.width / shape.width
        height_amount = self.height / shape.height
        return floor(width_amount * height_amount)
        # print('amount', (width_amount, height_amount))

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

    def __init__(self, length):
        Rectangle.__init__(self, length, length)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f'Square(side={self.width})'
