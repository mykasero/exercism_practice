class School:
    def __init__(self):
        self.s_g = dict()
        self.expected = []
        self.grades = []

    def add_student(self, name, grade):
        if name in self.s_g:
            self.expected.append(False)
        else:
            self.s_g[name] = self.s_g.get(grade, grade)
            self.expected.append(True)

    def roster(self):
        students = []
        self.grades = []
        if len(self.expected) < 1:
            return self.expected
        else:
            for student in self.s_g.keys():
                students.append(student)
            for grade in self.s_g.values():
                self.grades.append(grade)

            if len(set(self.grades)) == 1:
                students = []
                for stud_srtd in sorted(self.s_g.items(), key=lambda x: x[0]):
                    students.append(stud_srtd[0])

                which_if = "OPT1"
                return students

            elif len(set(self.grades)) == len(self.grades):
                students = []
                for stud_srtd in sorted(self.s_g.items(), key=lambda x: x[1]):
                    students.append(stud_srtd[0])

                which_if = "OPT2"
                return students

            else:
                which_if = "OPT3"
                students = []
                for stud_srtd in sorted(self.s_g.items(), key=lambda x: x[1]):
                    students.append(stud_srtd[0])

                sorted_dict = sorted(self.s_g.items(), key=lambda x: x[1])
                indv_grades = list(set(self.grades))

                split_list = []
                students = []

                for grade in indv_grades:
                    for key, value in sorted_dict:
                        if value == grade:
                            split_list.append(key)
                    students += sorted(split_list)
                    split_list = []

                return students

            return students

    def grade(self, grade_number):
        students = []
        if len(self.expected) < 1:
            return []
        else:
            if grade_number not in self.s_g.values():
                return []
            else:
                for key, value in self.s_g.items():
                    if grade_number == value:
                        students.append(key)

                return sorted(students)

    def added(self):
        if len(self.s_g.keys()) > 0:
            return self.expected

