from math_list import MathList
import unittest

# TODO: Напишите тесты для проверки каждой операции и метода класса Mathlist
# Подсказка: для проверок используйте assertEqual, assertTrue

# TODO: Write tests to test each operation and method of the Mathlist class
# Hint: use assertEqual, assertTrue


class MathListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = MathList([1, 2, 3])
        self.list2 = MathList([4, 5, 6])

    def test_sum(self):
        """Проверка суммы двух списков"""
        list_sum = self.list1 + self.list2
        self.assertEqual(
            list_sum.value,
            [5, 7, 9]
        )


if __name__ == '__main__':
    unittest.main()
