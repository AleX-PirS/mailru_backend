import unittest

from metaclass import CustomClass


class AttributeTest(unittest.TestCase):
    def setUp(self):
        self.obj = CustomClass()

    def test_result(self):
        self.assertFalse(hasattr(self.obj, "x"))
        self.assertFalse(hasattr(self.obj, "val"))
        self.assertFalse(hasattr(self.obj, "line"))

        self.assertTrue(hasattr(self.obj, "custom_x"))
        self.assertTrue(hasattr(self.obj, "custom_val"))
        self.assertTrue(hasattr(self.obj, "custom_line"))


if __name__ == "__main__":
    unittest.main()
