def importance_by_urgency(importance, urgency):
    if importance == 1 and urgency == 1:
        return 1
    if importance == 1 and urgency == 2:
        return 2
    if importance == 2 and urgency == 1:
        return 3
    if importance == 2 and urgency == 2:
        return 4