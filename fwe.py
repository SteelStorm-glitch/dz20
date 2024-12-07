#Функция для вычисления суммы чисел в списке:
def sum_of_list(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    return sum(numbers)
#Функция для нахождения уникальных элементов в списке:
def unique_elements(elements):
    return list(set(elements))
#Функция для нахождения наибольшего общего делителя (НОД):
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#Функция для нахождения второго по величине числа в списке:
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("Список должен содержать как минимум два уникальных числа.")
    unique_numbers.sort()
    return unique_numbers[-2]
#Автотесты
import unittest
class TestFunctions(unittest.TestCase):

    def test_sum_of_list(self):
        self.assertEqual(sum_of_list([1, 2, 3, 4]), 10)
        self.assertEqual(sum_of_list([-1, -2, -3]), -6)
        with self.assertRaises(ValueError):
            sum_of_list("Нет в списке")

    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(unique_elements(['a', 'b', 'a']), ['a', 'b'])

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)

    def test_second_largest(self):
        self.assertEqual(second_largest([1, 2, 3, 4]), 3)
        self.assertEqual(second_largest([4, 4, 3, 2]), 3)
        with self.assertRaises(ValueError):
            second_largest([1])

if __name__ == "__main__":
    unittest.main()
