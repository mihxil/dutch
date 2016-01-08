#!/usr/bin/env python3
import base

__author__ = 'mihxil'


class Dutch(base.Base):

    decimal = " komma"

    letters_tien = ["", "één", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]
    letters_twintig = ["tien", "elf", "twaalf", "dertien", "veertien"]
    letters_tig = ["nul", "tien", "twintig", "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig",
                   "negentig"]
    letters_big_pre = ["mil", "bil", "tril", "quadril", "quintil", "sextil", "septil", "octil", "nonil", "decil"]
    letters_big_post = ["joen", "jard"]

    def _number(self, a):
        if a < 0:
            return "min " + self._number(-1 * a)
        if a < 10:
            return self.letters_tien[a]
        if a < 15:
            return self.letters_twintig[a - 10]
        if a < 20:
            return self.letters_tien[a - 10] + "tien"
        if a < 100:
            begin = self._number(a % 10)
            if len(begin) > 0:
                if begin[-1] in 'aeio':
                    begin += "ën"
                else:
                    begin += "en"
            return begin + self.letters_tig[(a - a % 10) // 10]
        if a < 200:
            return "honderd" + self._number(a - 100)
        if a < 1000:
            first = a // 100
            return self._number(first) + "honderd" + self._number(a - first * 100)
        if a < 2000:
            return self.__join("duizend", self._number(a - 1000))
        if a < 10 ** 6:
            first = a // 1000
            return self.__join(self._number(first) + "duizend", self._number(a - first * 1000))
        else:
            rounded = a // 10 ** 6
            return self.__join(self._big(rounded, 2), self._number(a - rounded * 10 ** 6))

    def _big(self, rounded, mil_factor):
        if rounded == 0:
            return ""
        if rounded < 1000:
            return self.__join(self._number(rounded),
                               self.letters_big_pre[(mil_factor - 2) // 2] + self.letters_big_post[
                                  (mil_factor - 2) % 2])
        else:
            first = rounded // 1000
            return self.__join(
                    self._big(first, mil_factor + 1),
                    self._big(rounded - first * 1000, mil_factor)

            )

    def __join(self, pre, post):
        if len(post) > 0 and len(pre) > 0:
            return pre + " " + post
        else:
            return pre + post


import unittest


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.instance = Dutch()

    def testSmall(self):
        self.assertEqual("min tien", self.instance.number(-10))
        self.assertEqual("nul", self.instance.number(0))
        self.assertEqual("één", self.instance.number(1))
        self.assertEqual("twee", self.instance.number(2))
        self.assertEqual("drieëntwintig", self.instance.number(23))
        self.assertEqual("negentien", self.instance.number(19))
        self.assertEqual("negentien", self.instance.number(19))
        self.assertEqual("vijftien", self.instance.number(15))

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


    def testDecimal(self):
        self.assertEqual("twee komma drie", self.instance.number("2.3"))


if __name__ == "__main__":
    unittest.main()

