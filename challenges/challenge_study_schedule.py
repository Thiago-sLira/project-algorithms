def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students_online = 0
    for entry, exit in permanence_period:
        if not isinstance(entry, int) or not isinstance(exit, int):
            return None
        # student_range = list(range(entry, exit + 1))
        if entry <= target_time <= exit:
            students_online += 1

    return students_online


# period = [(2, 2), (1, 2), (2), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(period, 3))

# entry, exit = period[3]
# print(list(range(entry, exit + 1)))
