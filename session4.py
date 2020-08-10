import random
import decimal
from decimal import Decimal
import cmath

decimal.getcontext().prec = 10

# random.seed(100)


class Qualean(object):
    def __init__(self, q_value):
        if not (q_value in [-1, 0, 1]):
            raise ValueError("Check type of value passed")
        else:
            random_ = Decimal(str(random.uniform(-1, 1)))
            self.value = Decimal(str(q_value)) * random_
            # self.value = self.value.quantize(Decimal('1e-10'), rounding=decimal.ROUND_HALF_EVEN)

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.value + other.value

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.value >= other.value

    def __le__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value <= other.value

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value > other.value

    def __repr__(self):
        return f"'Qualean({self.value})'"

    def __str__(self):
        return f'{self.value}'

    def __bool__(self):
        return self.value != 0

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value == other.value

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value * other.value

    def __invertsign__(self):
        return -1 * self.value

    def __and__(self, other):
        if self.__bool__() and isinstance(other, Qualean) and other.__bool__():
            return True
        else:
            return False

    def __or__(self, other):
        if self.__bool__() or (isinstance(other, Qualean) and other.__bool__()):
            return True
        else:
            return False

    def __float__(self):
        return float(self.value)

    def __sqrt__(self):
        if self.value < 0:
            # return complex(0, Decimal.sqrt(self.__invertsign__()))
            return cmath.sqrt(self.value)
        else:
            return Decimal.sqrt(self.value)

    def __ne__(self, other):
        return not self.__eq__(other)

print(type(repr(Qualean(1))))