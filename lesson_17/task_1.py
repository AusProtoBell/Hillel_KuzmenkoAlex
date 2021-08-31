from lesson_6 import task_1 as dict_test
from lesson_7 import task_2 as temp
from lesson_11 import task_2 as palindrome
from lesson_15 import task_2 as phone_check
import unittest


class DictConstructTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(dict_test.dict_construct(
            (1, 2, 3, 4, 5), ("orange", "apple", "banana", "grapefruit", "watermelon")),
            {1: 'orange', 2: 'apple', 3: 'banana', 4: 'grapefruit', 5: 'watermelon'})


class TempTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(temp.temp_calc(36, 'C'), (36.0, 309.15, 96.8))
        self.assertEqual(temp.temp_calc(300, 'K'), (26.850000000000023, 300.0, 80.32999999999998))
        self.assertEqual(temp.temp_calc(15, 'F'), (-9.444444444444445, 263.7055555555556, 15.0))


class PalindromeTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(palindrome.palindrome_check("А роза упала на лапу Азора."), True)


class NumberTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(phone_check.format_number('+3806399-999-99'), "(+38) 063 999-99-99")


if __name__ == '__main__':
    unittest.main()
