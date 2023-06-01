period = [(2, 2), (1, 2), (2), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students_online = 0
    for entry, exit in permanence_period:
        if entry is None or exit is None:
            return None
        else:
            student_range = list(range(entry, exit + 1))
            if target_time in student_range:
                students_online += 1

    return students_online


print(study_schedule(period, 3))

# entry, exit = period[3]
# print(list(range(entry, exit + 1)))
