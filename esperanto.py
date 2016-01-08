#!/usr/bin/env python3
import base

__author__ = 'mihxil'


class Esperanto(base.Base):
    zero = "nulo"
    decimal = " komo"
    literoj = ["", "unu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "naŭ"]


    def _number(self, a):
        if a < 0:
            return "minus " + self._number(-1 * a)
        if a < 10:
            return self.literoj[a]
        if a < 100:
            return self.join(self.pre(a // 10) + "dek", self.literoj[a % 10])
        if a < 1000:
            return self.join(self.pre(a // 100) + "cent", self._number(a % 100))
        if a < 1000000:
            return self.join(self.pre(a // 1000) + "mil", self._number(a % 1000))

    def join(self, pre, post):
        if len(post) > 0:
            return pre + " " + post
        else:
            return pre

    def pre(self, a):
        if a == 1:
            return ""
        else:
            return self._number(a)


import unittest


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.instance = Esperanto()

    def testSmall(self):
        self.assertEqual("min dek", self.instance.number(-10))
        self.assertEqual("dek kvin", self.instance.number(15))
        self.assertEqual("kvardek naŭ", self.instance.number(49))

    def testBigger(self):
        self.assertEqual("cent kvindek", self.instance.number(150))
        self.assertEqual("kvincent kvindek", self.instance.number(550))
        self.assertEqual("mil kvincent kvindek", self.instance.number(1550))
        self.assertEqual("mil kvincent kvindek", self.instance.number(101550))


if __name__ == "__main__":
    unittest.main()

