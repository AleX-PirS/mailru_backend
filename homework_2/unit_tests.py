import unittest

from modifiedlist import ModifiedList


class SubAddTest(unittest.TestCase):
    def setUp(self):
        self.m_l_1 = ModifiedList([2, 3, 4, 5])
        self.m_l_2 = ModifiedList([3, 4, 5, 6])
        self.m_l_empty = ModifiedList([])
        self.l_1 = [1, 2, 3, 4]
        self.l_empty = []

    def test_result(self):
        self.assertEqual(type(self.m_l_1 - self.m_l_2), type(ModifiedList([])))
        self.assertEqual(type(self.m_l_1 + self.m_l_2), type(ModifiedList([])))
        self.assertEqual(type(self.l_1 - self.m_l_1), type(ModifiedList([])))
        self.assertEqual(type(self.m_l_1 - self.l_1), type(ModifiedList([])))
        self.assertEqual(type(self.l_1 + self.m_l_1), type(ModifiedList([])))
        self.assertEqual(type(self.m_l_1 + self.l_1), type(ModifiedList([])))
        self.assertEqual(self.m_l_1 - self.m_l_2, ModifiedList([-1, -1, -1, -1]))
        self.assertEqual(self.m_l_1 - self.m_l_empty, ModifiedList([2, 3, 4, 5]))
        self.assertEqual(self.m_l_empty - self.m_l_1, ModifiedList([-2, -3, -4, -5]))
        self.assertEqual(self.m_l_1 + self.m_l_2, ModifiedList([5, 7, 9, 11]))
        self.assertEqual(self.m_l_1 + self.m_l_empty, ModifiedList([2, 3, 4, 5]))
        self.assertEqual(self.l_empty - self.m_l_empty, ModifiedList([]))
        self.assertEqual(self.l_1 + self.m_l_1, ModifiedList([3, 5, 7, 9]))
        self.assertEqual(self.l_1 - self.m_l_1, ModifiedList([-1, -1, -1, -1]))
        self.assertEqual(self.m_l_1 - self.l_1, ModifiedList([1, 1, 1, 1]))


class CompareTest(unittest.TestCase):
    def setUp(self):
        self.m_l_1 = ModifiedList([2, 1, 3, 4])
        self.m_l_2 = ModifiedList([2, 3, 4])
        self.m_l_empty = ModifiedList([])
        self.l_1 = [10, -10, 3, 4]
        self.l_empty = []
        self.l_2 = [2, 1, 3, 4]
        self.l_3 = [10, -20, 5, -1]

    def test_result(self):
        self.assertTrue(self.m_l_1 > self.m_l_2)
        self.assertTrue(self.m_l_1 == self.l_2)
        self.assertTrue(self.m_l_1 >= self.l_2)
        self.assertTrue(self.m_l_empty == self.l_empty)
        self.assertTrue(self.m_l_empty > self.l_3)
        self.assertTrue(self.m_l_2 < self.l_2)
        self.assertTrue(self.l_3 != self.m_l_2)
        self.assertTrue(self.l_3 <= self.m_l_1)
        self.assertFalse(self.m_l_1 <= self.m_l_2)
        self.assertFalse(self.l_empty > self.m_l_1)
        self.assertFalse(self.m_l_1 != self.l_2)
        self.assertFalse(self.m_l_2 < self.l_3)
        self.assertFalse(self.m_l_1 == self.l_3)
        self.assertFalse(self.l_1 >= self.m_l_1)


if __name__ == "__main__":
    unittest.main()
