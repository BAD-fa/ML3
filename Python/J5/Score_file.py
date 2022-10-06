class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:

    def __init__(self):
        self.address = None

    def set_file(self, address):
        self.address = address

    def load(self, line_number) -> Grade | None:
        with open(self.address, "r") as f:
            lines = f.readlines()

            if line_number > len(lines):
                return None

            data = lines[line_number - 1].split(' ')
            return Grade(data[0], data[1], data[2])

    def calc_student_average(self, student_id):
        _sum = 0
        count = 0
        with open(self.address, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if data[0] == str(student_id):
                    _sum += float(data[2])
                    count += 1

        return _sum / count

    def calc_course_average(self, course_code):
        _sum = 0
        count = 0
        with open(self.address, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if data[1] == str(course_code):
                    _sum += float(data[2])
                    count += 1

        return _sum / count

    def count(self):
        with open(self.address, "r") as f:
            lines = f.readlines()

        return len(lines)

    def save(self, grade):
        with open(self.address, "a") as f:
            if f.tell():
                data = f"\n{grade.student_id} {grade.course_code} {grade.score}"
            else:
                data = f"{grade.student_id} {grade.course_code} {grade.score}"
            f.write(data)


if __name__ == "__main__":
    g1 = Grade(1, 1, 1)
    g2 = Grade(1, 2, 2)
    g3 = Grade(2, 1, 3)
    g4 = Grade(2, 2, 4)

    cu = CourseUtil()

    cu.set_file("score.txt")

    # cu.save(g1)
    # cu.save(g2)
    # cu.save(g3)
    # cu.save(g4)

    grade = cu.load(2)

    print(grade.student_id, grade.course_code, grade.score)

    print(cu.calc_course_average(1))

    print(cu.calc_student_average(2))
