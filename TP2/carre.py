from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, valeur):
        if valeur < 0:
            print("Erreur : La largeur ne peut pas être négative.")
        else:
            self._width = valeur

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, valeur):
        if valeur < 0:
            print("Erreur : La hauteur ne peut pas être négative.")
        else:
            self._height = valeur

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        return sqrt((self._width ** 2 + self._height ** 2))

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Trop grand pour faire une image"
        else:
            return ("*" * self._width + "\n") * self._height

    def get_amount_inside(self, other):
        return (self._width // other.width) * (self.height // other.height)

    def __str__(self):
        return f"Rectangle(largeur={self._width}, hauteur={self._height})"


class Carree(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self._width

    @side.setter
    def side(self, valeur):
        self._width = valeur
        self._height = valeur

    def __str__(self):
        return f"Carree(cote={self.side})"
