"""# Homework 5 - needs to be presented before exam day
#We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
Because of approximations in python the triangle will get distorted after some of the changes so this is not a
perfect model
30P
 - class constructor can receive 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
default value of 1)
class variables for sides will be called A, B, C
class variables for angles will be called AB, BC, CA (indicating sides)
30P
- class implements method to modify_angle:
  - modify_angle method takes two argument:
      - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
      - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
When an angel is modifies you will need to recalculate the opposing side which can be done using the following
example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
recalculated the opposite side using the following example:
angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),
30P
- class implements method to modify_side:
  - modify_side method takes two argument:
      - "side" and can be one of 3 string values 'A', 'B', 'C'
      - "meters" that can be a positive or negative and represents the amount by which the side will be modified
If as a result of the change sum of the unmodified sides is less than or equal to the changed side then method should
throw an exception
If as a result of the change side will be less than or equal to 0 then method should raise a different exception
When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
the same triangle angles. For example, if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C
10P
Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5
!!! HINT: results from functions in math module are usually in radians and you will need to import degree function
using a different name since you are asked to use an argument called degrees
"""

from math import cos, acos
from math import degrees as deg

from math import cos, acos
from math import degrees as deg


class Triangle:
    def __init__(self, A: float = 1, B: float = 1, C: float = 1, AB: float = 60, BC: float = 60, CA: float = 60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def modify_angle(self, angle: str, degrees: float):
        if angle == 'AB':
            self.AB += degrees
            self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB)) ** (1 / 2)
            self.BC = deg(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
            self.CA = deg(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))

        elif angle == 'BC':
            self.BC += degrees
            self.A = (self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(self.BC)) ** 0.5
            self.AB = deg(acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))
            self.CA = deg(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))

        elif angle == 'CA':
            self.CA += degrees
            self.B = (self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(self.CA)) ** 0.5
            self.AB = deg(acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))
            self.BC = deg(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))

        rules = [
            0 < self.AB < 180,
            0 < self.BC < 180,
            0 < self.CA < 180
        ]
        if not all(rules):
            raise ValueError('Total sum of all angles must be 180')

    def modify_side(self, side: str, meters: float):
        if side == 'A':
            temp = self.A
            self.A += meters

            if self.A >= self.B + self.C:
                raise ValueError("One side cannot be greated than the sum of other two sides")
            elif self.A <= 0:
                raise ValueError("Side of a triangle cannot be negative or 0")

            self.B = ((self.A) / temp) * self.B
            self.C = ((self.A) / temp) * self.C

        elif side == 'B':
            temp = self.B
            self.B += meters

            if self.B >= self.A + self.C:
                raise ValueError("One side cannot be greated than the sum of other two sides")
            elif self.B <= 0:
                raise ValueError("Side of a triangle cannot be negative or 0")

            self.A = ((self.B) / temp) * self.A
            self.C = ((self.B) / temp) * self.C

        elif side == 'C':
            temp = self.C
            self.C += meters

            if self.C >= self.B + self.A:
                raise ValueError("One side cannot be greated than the sum of other two sides")
            elif self.C <= 0:
                raise ValueError("Side of a triangle cannot be negative or 0")

            self.B = ((self.C) / temp) * self.B
            self.A = ((self.C) / temp) * self.A


if __name__ == "__main__":
    my_triangle = Triangle()
    my_triangle.modify_angle('AB', 30)
    my_triangle.modify_side('A', 1.5)
    print("AB", my_triangle.AB)
    print("BC", my_triangle.BC)
    print("CA", my_triangle.CA)
    print("A", my_triangle.A)
    print("B", my_triangle.B)
    print("C", my_triangle.C)


