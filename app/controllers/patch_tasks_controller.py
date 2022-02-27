from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.eisenhowers_model import EisenhowerModel
from app.models.exc import Eisenhower_Error
from app.models.tasks_model import TasksModel
from app.services.data_categories_to_patch import data_categories_to_patch
from app.services.data_to_pactch import data_to_patch
from app.services.importance_by_urgency import importance_by_urgency
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError


def patch_tasks(id):
    try:
        data = request.get_json()
        query = TasksModel.query.get_or_404(id)

        if 'name' in data.keys():
            data['name'] = data['name'].title()
        
        if 'importance' in data.keys():
            importance = data['importance']
        else:
            importance = query.importance
        
        if 'urgency' in data.keys():
            urgency = data['urgency']
        else:
            urgency = query.urgency
        
        eisenhower = importance_by_urgency(importance, urgency)

        eise_query = EisenhowerModel.query.filter_by(id=eisenhower).one()
        data['eisenhowers_id'] = eisenhower

        if eisenhower == False:
            raise Eisenhower_Error
        
        
        data_categories_to_patch(data)
        data_to_patch(query, data)

        list_task = query.__dict__.copy()

        list_task['classification'] = eise_query.type

        list_task['categories'] = []

        for category in query.categories:
            list_task['categories'].append(category.name)

        
        del list_task['_sa_instance_state']
        del list_task['importance']
        del list_task['urgency']
        del list_task['eisenhowers_id']

        current_app.db.session.add(query)
        current_app.db.session.commit()

        return jsonify(list_task), HTTPStatus.CREATED

    
    except NotFound:
        return {'error': 'Task not found!'}, HTTPStatus.NOT_IMPLEMENTED
    
    except Eisenhower_Error as e:
        return e.eisenhower_err_description(importance, urgency), e.code
    
    except IntegrityError:
        return {'error': 'Task already exists'}, HTTPStatus.CONFLICT