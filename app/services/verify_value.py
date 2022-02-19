from app.models.exc import BadRequestValue 


def verify_value(importance, urgency):
    if importance > 2 or urgency > 2:
        raise BadRequestValue