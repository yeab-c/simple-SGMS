SUBJECTS = ["Mathematics", "English", "Science"]


def validate_mark(mark):
    return (
        isinstance(mark, (int, float))
        and not isinstance(mark, bool)
        and 0 <= mark <= 100
    )


def average(marks):
    if not marks or not all(validate_mark(m) for m in marks):
        raise ValueError("Marks must be numbers from 0 to 100")
    return sum(marks) / len(marks)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"
