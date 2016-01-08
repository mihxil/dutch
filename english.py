#!/usr/bin/env python3
import base

__author__ = 'mihxil'


class English(base.Base):
    decimal = " point"
    zero = "zero"

    letters_tien = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    letters_twintig = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
    letters_tig = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
                   "ninety"]
    letters_big_pre = ["mil", "bil", "tril", "quadril", "quintil", "sextil", "septil", "octil", "nonil", "decil"]
    letters_big_post = ["lion", "liard"]



    def _number(self, a):
        if a < 0:
            return "minus " + self._number(-1 * a)
        if a < 10:
            return self.letters_tien[a]
        if a < 15:
            return self.letters_twintig[a - 10]
        if a < 100:
            begin = self._number(a % 10)
            if len(begin) > 0:
                begin = " " + begin
            return self.letters_tig[(a - a % 10) // 10] + begin
        if a < 200:
            return " hundred " + self._number(a - 100)
        if a < 1000:
            first = a // 100
            return self._number(first) + " hundred " + self._number(a - first * 100)
        if a < 2000:
            return self._join(" thousand", self._number(a - 1000))
        if a < 10 ** 6:
            first = a // 1000
            return self._join(self._number(first) + " thousand", self._number(a - first * 1000))
        else:
            rounded = a // 10 ** 6
            return self._join(self._big(rounded, 2), self._number(a - rounded * 10 ** 6))

    def _big(self, rounded, mil_factor):
        if rounded == 0:
            return ""
        if rounded < 1000:
            return self._join(self._number(rounded),
                              self.letters_big_pre[(mil_factor - 2) // 2] + self.letters_big_post[
                                  (mil_factor - 2) % 2])
        else:
            first = rounded // 1000
            return self._join(
                    self._big(first, mil_factor + 1),
                    self._big(rounded - first * 1000, mil_factor)

            )

    def _join(self, pre, post):
        if len(post) > 0 and len(pre) > 0:
            return pre + " " + post
        else:
            return pre + post


import unittest


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.instance = English()

    def testSmall(self):
        self.assertEqual("minus ten", self.instance.number(-10))
        self.assertEqual("zero", self.instance.number(0))
        self.assertEqual("one", self.instance.number(1))
        self.assertEqual("two", self.instance.number(2))
        self.assertEqual("twenty three", self.instance.number(23))

    def testFraction(self):
        self.assertEqual("two point five", self.instance.number(2.5))

    def testBigger(self):
        self.assertEqual("honderddrieëntwintigduizend vijfhonderdéénenzestig", self.instance.number(123561))

    def testBig(self):
        self.assertEquals("één miljoen", self.instance._big(1, 2))
        self.assertEquals("tien miljoen", self.instance._big(10, 2))
        self.assertEquals("één miljard", self.instance._big(1000, 2))
        self.assertEquals("één miljard honderd miljoen", self.instance._big(1100, 2))

    def testBiggerNumber(self):
        self.assertEqual("één deciljard",
                         self.instance.number(10 ** 63))
        print(self.instance.number(111232123561))
        self.assertEqual(
            "honderdelf miljard tweehonderdtweeëndertig miljoen honderddrieëntwintigduizend vijfhonderdéénenzestig",
            self.instance.number(111232123561))


        print(self.instance.number(111232123561234098354098309548093343432809))


if __name__ == "__main__":
    unittest.main()
