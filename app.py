from grades import SUBJECTS, validate_mark, average, letter_grade
from db import connect, add_student, get_students


def ask_mark(subject):
    while True:
        try:
            value = float(input(f"  {subject} mark (0-100): "))
        except ValueError:
            print("Enter a number.")
            continue
        if validate_mark(value):
            return value
        print("Mark must be between 0 and 100.")


def add_flow(conn):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    marks = [ask_mark(subject) for subject in SUBJECTS]
    avg = average(marks)
    grade = letter_grade(avg)
    add_student(conn, name, marks, avg, grade)
    print(f"Saved: {name}, average {avg:.1f}, grade {grade}")


def show_flow(conn):
    rows = get_students(conn)
    if not rows:
        print("No students yet.")
        return
    header = f"{'Name':<15}"
    header += "".join(f"{s:<13}" for s in SUBJECTS)
    header += f"{'Average':<10}Grade"
    print(header)
    for name, math, eng, prog, avg, grade in rows:
        print(f"{name:<15}{math:<13.1f}{eng:<13.1f}{prog:<13.1f}{avg:<10.1f}{grade}")


def main():
    conn = connect()
    while True:
        choice = input("\n1) Add student  2) Show results  3) Quit: ").strip()
        if choice == "1":
            add_flow(conn)
        elif choice == "2":
            show_flow(conn)
        elif choice == "3":
            break
        else:
            print("Choose 1, 2 or 3.")
    conn.close()


if __name__ == "__main__":
    main()
