2


class Fraction:

    def __init__(self, integer=0, fr_up=0, fr_down=1):
        self.integer = integer
        self.fr_up = fr_up
        self.fr_down = fr_down
        if fr_up < 0 and abs(fr_up) < fr_down:
            self.integer -= 1
            self.fr_up = self.fr_down + fr_up
        if abs(fr_up) >= fr_down:
            self.integer += fr_up // fr_down
            self.fr_up = fr_up % fr_down

    def __add__(self, other):
        self_fr_down = self.fr_down
        self_fr_up = self.fr_up
        other_fr_down = other.fr_down
        other_fr_up = other.fr_up
        # We don't wanna to change
        # our variables
        if self.fr_down != other.fr_down:
            self_fr_down *= other.fr_down
            self_fr_up *= other.fr_down
            other_fr_down *= self.fr_down
            other_fr_up *= self.fr_down
        # Easy way to bring
        # to a common denominator
        return Fraction(self.integer + \
                        other.integer,
                        self_fr_up + \
                        other_fr_up,
                        self_fr_down)

    def __sub__(self, other):
        self_fr_down = self.fr_down
        self_fr_up = self.fr_up
        other_fr_down = other.fr_down
        other_fr_up = other.fr_up
        # We don't wanna to change
        # our variables
        if self.fr_down != other.fr_down:
            self_fr_down *= other.fr_down
            self_fr_up *= other.fr_down
            other_fr_down *= self.fr_down
            other_fr_up *= self.fr_down
        # Easy way to bring
        # to a common denominator
        return Fraction(self.integer - \
                        other.integer,
                        self_fr_up - \
                        other_fr_up,
                        self_fr_down)



    def __lt__(self, other):
        self_fr_up = self.fr_up
        self_fr_down = self.fr_down
        other_fr_up = other.fr_up
        other_fr_down = other.fr_down
        if self.fr_down != other.fr_down:
            self_fr_down *= other.fr_down
            self_fr_up *= other.fr_down
            other_fr_down *= self.fr_down
            other_fr_up *= self.fr_down
        if self.integer < other.integer:
            return True
        elif self.integer > other.integer:
            return False
        if self_fr_up < other_fr_up:
            return True
        else:
            return False

    def __gt__(self, other):
        self_fr_up = self.fr_up
        self_fr_down = self.fr_down
        other_fr_up = other.fr_up
        other_fr_down = other.fr_down
        if self.fr_down != other.fr_down:
            self_fr_down *= other.fr_down
            self_fr_up *= other.fr_down
            other_fr_down *= self.fr_down
            other_fr_up *= self.fr_down
        if self.integer > other.integer:
            return True
        elif self.integer < other.integer:
            return False
        if self_fr_up > other_fr_up:
            return True
        else:
            return False

    def __int__(self):
        try:
            mul = self.integer / abs(self.integer)
        # positive or negative?
        except ZeroDivisionError:
            mul = 1
        return self.integer + (self.fr_down - self.fr_up >= self.fr_up) * mul

    def __float__(self):
        return self.integer + self.fr_up / self.fr_down

    def __str__(self):
        return str(self.integer) + ' ' + \
               str(self.fr_up) + '/' + \
               str(self.fr_down)

    def __nonzero__(self):
        return True if self.integer or self.fr_up else False


f1 = Fraction(3, 2, 3)
f2 = Fraction(1, 1, 3)
res = bool(f2)
print(Fraction.__add__(f1, f2))
print(Fraction.__sub__(f1, f2))
print(Fraction.__gt__(f1, f2))
print(Fraction.__lt__(f1, f2))
