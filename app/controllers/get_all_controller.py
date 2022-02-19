from flask import jsonify
from http import HTTPStatus
from app.models.categories_model import CategoriesModel
from app.models.eisenhowers_model import EisenhowerModel
from app.services.importance_by_urgency import importance_by_urgency


def get_all():
        categories = CategoriesModel.query.all()
        categories_tasks = []

        for category in categories:
            data = {}

            data['id'] = category.id
            data['name'] = category.name
            data['description'] = category.description
            data['tasks'] = []

            for task in category.tasks:
                data_task = {}
                data_task['id'] = task.id
                data_task['name'] = task.name
                data_task['description'] = task.description
                data_task['duration'] = task.duration
                data_task['classification'] = EisenhowerModel.query.filter_by(id = importance_by_urgency(task.importance, task.urgency)).one().__dict__.get('type')
                
                data['tasks'].append(data_task)

            categories_tasks.append(data)

        return jsonify(categories_tasks), HTTPStatus.CREATED