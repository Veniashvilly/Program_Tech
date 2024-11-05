import unittest
def f(x,y):
    return x + y
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(f(1, 4), 5)

    def test2(self):
        self.assertEqual(f(-10, 3), -7)

    def test3(self):
        self.assertEqual(f(5, 5), 0)

if __name__ == "__main__":
    unittest.main()