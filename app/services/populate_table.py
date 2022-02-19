from sqlalchemy.orm import Session
from flask import current_app
from app.models.eisenhowers_model import EisenhowerModel


def populate_table():
    if not EisenhowerModel.query.first():
        session: Session = current_app.db.session
    
        patterns_values = ['Do It First', 'Delegate It', 'Schedule It', 'Delete It']
        eisenhowers = [EisenhowerModel(type=pattern) for pattern in patterns_values]

        session.add_all(eisenhowers)
        session.commit()