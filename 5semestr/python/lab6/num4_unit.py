import unittest

# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]


class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
    
    def test_single(self):
        self.assertEqual(reverse('a'), 'a')
    
    def test_palindrom(self):
        self.assertEqual(reverse('aba'), 'aba')

    def test_normal(self):
        self.assertEqual(reverse('abc'), 'cba')
        
    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)
    
    def test_wrong_type2(self):
        with self.assertRaises(TypeError):
            reverse(["a","b","c"])


if __name__ == '__main__':
    unittest.main()