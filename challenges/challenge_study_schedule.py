period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
    for entry, exit in permanence_period:
        student_range = list(range(entry, exit + 1))
        print(student_range)


(study_schedule(period, 5))

entry, exit = period[3]
print(list(range(entry, exit + 1)))
