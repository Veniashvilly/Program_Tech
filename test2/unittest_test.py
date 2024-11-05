import unittest
def is_non_decreasing_tree(n, lst):
    flag = 0
    for i in range(n // 2):
        lft_chld = 2 * i + 1
        rght_chld = 2 * i + 2
        if lft_chld < n and lst[i] > lst[lft_chld]:
            flag = 1
            break
        if rght_chld < n and lst[i] > lst[rght_chld]:
            flag = 1
            break
    return "NO" if flag == 1 else "YES"

class TestNonDecreasingTree(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_non_decreasing_tree(3, [1, 2, 3]), "YES")

    def test2(self):
        self.assertEqual(is_non_decreasing_tree(3, [3, 2, 1]), "NO")

    def test3(self):
        self.assertEqual(is_non_decreasing_tree(5, [1, 2, 3, 4, 5]), "YES")

    def test4(self):
        self.assertEqual(is_non_decreasing_tree(4, [1, 3, 2, 4]), "NO")

if __name__ == "__main__":
    unittest.main()