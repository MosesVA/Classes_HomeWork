class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    def get_name(self):
        return self._name

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    def set_experience(self, new_experience):
        self._experience = new_experience

    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} лет."

    def add_mark(self, student_name, value):
        return f"{self._name} поставил оценку {value} студенту {student_name}."

    def remove_mark(self, student_name, value):
        return f"{self._name} удалил оценку {value} студенту {student_name}."

    def give_a_consultation(self, student_class):
        return f"{self._name} провел консультацию в классе {student_class}."


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    def get_teacher_data(self):
        return (f"{self._name}, образование {self._education}, опыт работы {self._experience} лет. "
                f"Предмет {self._discipline}, Должность {self._job_title}")

    def add_mark(self, student_name, value):
        return f"{self._name} поставил оценку {value} студенту {student_name}. Предмет: {self._discipline}."

    def remove_mark(self, student_name, value):
        return f"{self._name} удалил оценку {value} студенту {student_name}.  Предмет: {self._discipline}."

    def give_a_consultation(self, student_class):
        return (f"{self._name} провел консультацию в классе {student_class}. "
                f"По предмету {self._discipline} как {self._job_title}")


ivan_petrov = Teacher("Иван Петров", "СПбГУ", 10)
print(ivan_petrov.get_name())
print(ivan_petrov.get_education())
print(ivan_petrov.get_experience())
ivan_petrov.set_experience(11)
print(ivan_petrov.get_teacher_data())
print(ivan_petrov.add_mark("Марк", 4))
print(ivan_petrov.remove_mark("Елена", 2))
print(ivan_petrov.give_a_consultation("7Б"))
print()
elena_ivanova = DisciplineTeacher("Елена Иванова", "ТюмГУ", 15, "Математика", "Учитель")
print(elena_ivanova.get_name())
print(elena_ivanova.get_education())
print(elena_ivanova.get_experience())
elena_ivanova.set_experience(16)
print(elena_ivanova.get_teacher_data())
print(elena_ivanova.add_mark("Клава", 5))
print(elena_ivanova.remove_mark("Теодор", 3))
print(elena_ivanova.give_a_consultation("8А"))
