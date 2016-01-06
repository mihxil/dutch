__author__ = 'mihxil'


class English:
    letters_tien = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    letters_twintig = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
    letters_tig = ["", "ten", "twinty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
                   "ninety"]
    letters_big_pre = ["mil", "bil", "tril", "quadril", "quintil", "sextil", "septil", "octil", "nonil", "decil"]
    letters_big_post = ["joen", "jard"]


    @staticmethod
    def number(a):
        """
        Returns a number in english
        :param a:
        :return:
        """
        if isinstance(a, str):
            a = float(a)

        if isinstance(a, int) or a.is_integer():
            if a == 0:
                return "nul"
            else:
                return English._number(int(a))
        else:
            result = English.number(int(a)) + " komma"
            if a < 0:
                a *= -1
                for c in str(a).split(".")[1]:
                    result += " " + English.number(int(c))
            return result

    @staticmethod
    def _number(a):
        if a < 0:
            return "min " + English._number(-1 * a)
        if a < 10:
            return English.letters_tien[a]
        if a < 15:
            return English.letters_twintig[a - 10]
        if a < 100:
            begin = English._number(a % 10)
            if len(begin) > 0:
                begin = " " + begin
            return English.letters_tig[(a - a % 10) // 10] + begin
        if a < 200:
            return " hundred " + English._number(a - 100)
        if a < 1000:
            first = a // 100
            return English._number(first) + "hundred " + English._number(a - first * 100)
        if a < 2000:
            return English.join("thousand", English._number(a - 1000))
        if a < 10 ** 6:
            first = a // 1000
            return English.join(English._number(first) + "thousand", English._number(a - first * 1000))
        else:
            rounded = a // 10 ** 6
            return English.join(English.dutch_big(rounded, 2), English._number(a - rounded * 10 ** 6))

    @staticmethod
    def dutch_big(rounded, mil_factor):
        if rounded == 0:
            return ""
        if rounded < 1000:
            return English.join(English._number(rounded),
                              English.letters_big_pre[(mil_factor - 2) // 2] + English.letters_big_post[
                                  (mil_factor - 2) % 2])
        else:
            first = rounded // 1000
            return English.join(
                    English.dutch_big(first, mil_factor + 1),
                    English.dutch_big(rounded - first * 1000, mil_factor)

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
        self.assertEqual("min tien", English.number(-10))
        self.assertEqual("nul", English.number(0))
        self.assertEqual("één", English.number(1))
        self.assertEqual("twee", English.number(2))
        self.assertEqual("drieëntwintig", English.number(23))

    def testBigger(self):
        self.assertEqual("honderddrieëntwintigduizend vijfhonderdéénenzestig", English.number(123561))

    def testBig(self):
        self.assertEquals("één miljoen", English.dutch_big(1, 2))
        self.assertEquals("tien miljoen", English.dutch_big(10, 2))
        self.assertEquals("één miljard", English.dutch_big(1000, 2))
        self.assertEquals("één miljard honderd miljoen", English.dutch_big(1100, 2))

    def testBiggerNumber(self):
        self.assertEqual("één deciljard",
                         English.number(10 ** 63))
        print(English._number(111232123561))
        self.assertEqual(
            "honderdelf miljard tweehonderdtweeëndertig miljoen honderddrieëntwintigduizend vijfhonderdéénenzestig",
            English.number(111232123561))


        print(English.number(111232123561234098354098309548093343432809))
