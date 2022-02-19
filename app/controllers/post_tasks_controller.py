from http import HTTPStatus
from flask import current_app, request
from app.models.categories_model import CategoriesModel
from app.models.eisenhowers_model import EisenhowerModel
from app.models.exc import BadRequestValue
from app.models.tasks_model import TasksModel
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from app.services.importance_by_urgency import importance_by_urgency
from app.services.verify_value import verify_value
from app.services.populate_table import populate_table

def post_task():
    populate_table()
    data = request.get_json()

    new_category = data.pop("categories")
    importance = data["importance"]
    urgency = data["urgency"] 

    new_classification = importance_by_urgency(importance, urgency)
    
    data["eisenhower_id"] = new_classification

    try:
        verify_value(importance, urgency)
        filter_eisenhower = EisenhowerModel.query.filter_by(id = new_classification).one()
        classification = (filter_eisenhower.__dict__.get('type'))
        new_task = TasksModel(**data)
        for category in new_category:
            try: 
                category = CategoriesModel.query.filter_by(name = category.Title()).one()
                new_task.categories.append(category)

            except:
                new_category = CategoriesModel(name=category.Title())
                current_app.db.session.add(new_category)
                current_app.db.session.commit()
                category = CategoriesModel.query.filter_by(name = category.Title()).one()
                new_task.categories.append(category)

            current_app.db.session.add(new_task)
            current_app.db.session.commit()

        return {
            "id": new_task.id,
            "name": new_task.name,
            "description":new_task.description,
            "duration": new_task.duration,
            "classification": classification,
            "categories": [category.name for category in new_task.categories]
        }, HTTPStatus.OK

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"msg": "task already exists!"}, HTTPStatus.CONFLICT

    except BadRequestValue:
        return {"msg": 
            { "valid_options": {
            "importance": [1, 2],
            "urgency": [1, 2]
            },
            "recieved_options": {
            "importance": importance,
            "urgency": urgency
            }}}, HTTPStatus.BAD_REQUEST