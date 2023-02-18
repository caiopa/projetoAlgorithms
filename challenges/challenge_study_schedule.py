def study_schedule(permanence_period, target_time):
    count = 0
    time = target_time
    try:
        for start, end in permanence_period:
            if time >= start and time <= end:
                count = count + 1
        return count
    except TypeError:
        return None