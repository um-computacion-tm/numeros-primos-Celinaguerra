import unittest

def is_primo(valor):
    divisor = valor - 1
    while divisor > 1:
        if valor%divisor == 0:
            return False
        divisor = divisor -1
    return True

class TestModule(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertTrue(result)

    def test_2(self):
        result = is_primo(2)
        self.assertTrue(result)

    def test_3(self):
        result = is_primo(3)
        self.assertTrue(result)

    def test_4(self):
        result = is_primo(4)
        self.assertFalse(result)

    def test_9(self):
        result = is_primo(9)
        self.assertFalse(result)

    def test_17(self):
        result = is_primo(17)
        self.assertTrue(result)


unittest.main()