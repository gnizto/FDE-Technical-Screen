import unittest
from main import sort

class TestSortFunction(unittest.TestCase):

    def test_standard_small_and_light_package(self):
        self.assertEqual(sort(50, 40, 30, 10), "STANDARD")

    def test_special_due_to_large_dimension(self):
        self.assertEqual(sort(200, 30, 20, 10), "SPECIAL")

    def test_special_due_to_heavy_weight(self):
        self.assertEqual(sort(50, 40, 30, 25), "SPECIAL")

    def test_special_due_to_large_volume(self):
        self.assertEqual(sort(200, 200, 200, 10), "SPECIAL")

    def test_rejected_heavy_and_bulky(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_special_due_to_dimension_equal_150(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_special_due_to_dimension_150_mass_below_heavy(self):
        self.assertEqual(sort(10, 150, 10, 19.9), "SPECIAL")

    def test_special_due_to_mass_equal_20(self):
        self.assertEqual(sort(10, 10, 10, 20.0), "SPECIAL")

    def test_rejected_due_to_volume_and_mass_at_limit(self):
        self.assertEqual(sort(100, 100, 100, 20.0), "REJECTED")

    def test_standard_just_below_volume_and_mass_limit(self):
        self.assertEqual(sort(100, 100, 99.99, 19.99), "STANDARD")

    def test_special_high_volume_but_mass_below_heavy(self):
        self.assertEqual(sort(149.99, 149.99, 149.99, 19.99), "SPECIAL")

    def test_special_at_volume_and_dimension_limit_mass_below_heavy(self):
        self.assertEqual(sort(150, 150, 150, 19.99), "SPECIAL")

    def test_rejected_high_volume_and_mass(self):
        self.assertEqual(sort(149.9, 149.9, 149.9, 20.0), "REJECTED")

    def test_standard_tiny_package(self):
        self.assertEqual(sort(1, 1, 1, 0.01), "STANDARD")

if __name__ == '__main__':
    unittest.main()
