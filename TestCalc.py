from unittest import TestCase  # 这里是计算器

from calc import Calc


class TestCalc(TestCase):
    # -------------------加法----------------------------
    def testAdd0(self):
        a = 6
        b = 5
        c = 111

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c, msg='过')

    def testAdd1(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd2(self):
        a = 6
        b = -5
        c = 1

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd3(self):
        a = -6
        b = -5
        c = -11

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd4(self):
        a = 'a'
        b = -5
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd5(self):
        a = 2
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd5(self):
        a = 'a'
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd6(self):
        a = 0
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd7(self):
        a = 0
        b = 8
        c = 8

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd8(self):
        a = 5
        b = 0
        c = 5

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd9(self):
        a = 's'
        b = 0
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    # ----------------减法------------------------

    def testMinus0(self):
        a = 6
        b = 5
        c = 1

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus1(self):
        a = -6
        b = 5
        c = -11

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus2(self):
        a = 6
        b = -5
        c = 11

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus3(self):
        a = -6
        b = -5
        c = -1

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus4(self):
        a = 'a'
        b = -5
        c = 'error'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus5(self):
        a = 2
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus5(self):
        a = 'a'
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus6(self):
        a = 0
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus7(self):
        a = 0
        b = 8
        c = -8

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus8(self):
        a = 5
        b = 0
        c = 5

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testMinus9(self):
        a = 's'
        b = 0
        c = 'error'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    # -------------------------乘法-------------------------
    def testmulti0(self):
        a = 6
        b = 5
        c = 30

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti1(self):
        a = -6
        b = 5
        c = -30

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti2(self):
        a = 6
        b = -5
        c = -30

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti3(self):
        a = -6
        b = -5
        c = 30

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti4(self):
        a = 'a'
        b = -5
        c = 'error'

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti5(self):
        a = 2
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti5(self):
        a = 'a'
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti6(self):
        a = 0
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti7(self):
        a = 0
        b = 8
        c = 0

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti8(self):
        a = 5
        b = 0
        c = 'error'

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testmulti9(self):
        a = 's'
        b = 0
        c = 'error'

        calc = Calc.multi()
        result = calc.add(a, b)

        self.assertEqual(result, c)

        # ------------------------除法--------------------

    def testdevision0(self):
        a = 5
        b = 5
        c = 1

        calc = Calc()
        result = calc.multi(a, b)

        self.assertEqual(result, c)

    def testdevision1(self):
        a = -5
        b = 5
        c = -1

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision2(self):
        a = 5
        b = -5
        c = -1

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision3(self):
        a = -5
        b = -5
        c = 1

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision4(self):
        a = 'a'
        b = -5
        c = 'error'

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision5(self):
        a = 2
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision5(self):
        a = 'a'
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision6(self):
        a = 0
        b = 'b'
        c = 'error'

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision7(self):
        a = 0
        b = 8
        c = 0

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision8(self):
        a = 5
        b = 0
        c = 'error'

        calc = Calc()
        result = calc.devision(a, b)

        self.assertEqual(result, c)

    def testdevision9(self):
        a = 's'
        b = 0
        c = 'error'

        calc = Calc.devision()
        result = calc.add(a, b)

        self.assertEqual(result, c)
