__author__ = 'mihxil'


class Dutch:
    letters_tien = ["", "één", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]
    letters_twintig = ["tien", "elf", "twaalf", "dertien", "veertien"]
    letters_tig = ["nul", "tien", "twintig", "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig",
                   "negentig"]
    letters_big_pre = ["mil", "bil", "tril", "quadril", "quintil", "sextil", "septil", "octil", "nonil", "decil"]
    letters_big_post = ["joen", "jard"]

    @staticmethod
    def number(a):
        if a < 10:
            return Dutch.letters_tien[a]
        if a < 15:
            return Dutch.letters_twintig[a - 10]
        if a < 100:
            begin = Dutch.number(a % 10)
            if len(begin) > 0:
                if begin[-1] in 'aeio':
                    begin += "ën"
                else:
                    begin += "en"
            return begin + Dutch.letters_tig[(a - a % 10) // 10]
        if a < 200:
            return "honderd" + Dutch.number(a - 100)
        if a < 1000:
            first = a // 100
            return Dutch.number(first) + "honderd" + Dutch.number(a - first * 100)
        if a < 2000:
            return "duizend" + Dutch.number(a - 1000)
        if a < 10 ** 6:
            first = a // 1000
            return Dutch.number(first) + "duizend" + Dutch.number(a - first * 1000)
        else:
            rounded = a // 10 ** 6
            return Dutch.join(Dutch.dutch_big(rounded, 2), Dutch.number(a - rounded * 10 ** 6))

    @staticmethod
    def dutch_big(rounded, mil_factor):
        if rounded == 0:
            return ""
        if rounded < 1000:
            return Dutch.join(Dutch.number(rounded),
                              Dutch.letters_big_pre[(mil_factor - 2) // 2] + Dutch.letters_big_post[
                                  (mil_factor - 2) % 2])
        else:
            first = rounded // 1000
            return Dutch.join(
                    Dutch.dutch_big(first, mil_factor + 1),
                    Dutch.dutch_big(rounded - first * 1000, mil_factor)

            )

    @staticmethod
    def join(pre, post):
        if len(post) > 0 and len(pre) > 0:
            return pre + " " + post
        else:
            return pre + post


import unittest


class TestMethods(unittest.TestCase):
    def testSmall(self):
        self.assertEqual("één", Dutch.number(1))
        self.assertEqual("twee", Dutch.number(2))
        self.assertEqual("drieëntwintig", Dutch.number(23))

    def testBigger(self):
        self.assertEqual("honderddrieëntwintigduizendvijfhonderdéénenzestig", Dutch.number(123561))

    def testBig(self):
        self.assertEquals("één miljoen", Dutch.dutch_big(1, 2))
        self.assertEquals("tien miljoen", Dutch.dutch_big(10, 2))
        self.assertEquals("één miljard", Dutch.dutch_big(1000, 2))
        self.assertEquals("één miljard honderd miljoen", Dutch.dutch_big(1100, 2))

    def testBiggerNumber(self):
        self.assertEqual("één deciljard",
                         Dutch.number(10 ** 63))
        print(Dutch.number(111232123561))
        self.assertEqual(
            "honderdelf miljard tweehonderdtweeëndertig miljoen honderddrieëntwintigduizendvijfhonderdéénenzestig",
            Dutch.number(111232123561))