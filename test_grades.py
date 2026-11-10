import unittest
from grades import SUBJECTS, validate_mark, average, letter_grade
from db import connect, add_student, get_students


class TestGrades(unittest.TestCase):
    def test_three_subjects(self):
        self.assertEqual(len(SUBJECTS), 3)

    def test_valid_mark(self):
        self.assertTrue(validate_mark(50))

    def test_negative_mark(self):
        self.assertFalse(validate_mark(-1))

    def test_mark_over_100(self):
        self.assertFalse(validate_mark(101))

    def test_non_number(self):
        self.assertFalse(validate_mark("abc"))

    def test_bool_mark(self):
        self.assertFalse(validate_mark(True))

    def test_average(self):
        self.assertEqual(average([80, 90, 100]), 90)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_average_invalid(self):
        with self.assertRaises(ValueError):
            average([50, 120, 70])

    def test_grade_a(self):
        self.assertEqual(letter_grade(95), "A")

    def test_grade_boundary(self):
        self.assertEqual(letter_grade(70), "C")

    def test_grade_fail(self):
        self.assertEqual(letter_grade(59.9), "F")

    def test_database(self):
        conn = connect(":memory:")
        add_student(conn, "Yeab", [80, 90, 85], 85.0, "B")
        self.assertEqual(
            get_students(conn), [("Yeab", 80.0, 90.0, 85.0, 85.0, "B")]
        )


if __name__ == "__main__":
    unittest.main()
