import abc
__author__ = 'mihxil'


class Base:


    def number(self, a):
        if isinstance(a, str):
            a = float(a)

        if isinstance(a, int) or a.is_integer():
            if a == 0:
                return self.zero
            else:
                return self._number(int(a))
        else:
            result = self.number(int(a)) + self.decimal
            if a < 0:
                a *= -1
            for c in str(a).split(".")[1]:
                result += " " + self.number(int(c))
            return result

    @abc.abstractmethod
    def _number(self, a):
        return

