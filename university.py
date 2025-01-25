class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age} років)"


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    selected_teachers = []

    while uncovered_subjects:
        # Знаходимо викладача, який може викладати найбільше непокритих предметів
        best_teacher = None
        best_coverage = 0

        for teacher in teachers:
            # Знаходимо предмети, які викладач може покрити
            can_cover = teacher.can_teach_subjects & uncovered_subjects
            if len(can_cover) > best_coverage or (
                len(can_cover) == best_coverage
                and (best_teacher is None or teacher.age < best_teacher.age)
            ):
                best_teacher = teacher
                best_coverage = len(can_cover)

        if not best_teacher:
            return None

        # Додаэмо викладача до розкладу
        if best_teacher not in selected_teachers:
            selected_teachers.append(best_teacher)

        best_teacher.assigned_subjects = (
            best_teacher.can_teach_subjects & uncovered_subjects
        )
        # Видалити ці предмети з множини непокритих
        uncovered_subjects -= best_teacher.assigned_subjects

    # Додати викладачів, які не отримали призначення
    for teacher in teachers:
        if teacher not in selected_teachers:
            selected_teachers.append(teacher)

    return selected_teachers
