from http import HTTPStatus
from flask import current_app
from app.models.tasks_model import TasksModel


def delete_tasks(id):
    task = TasksModel.query.get(id)

    if not task:
        return {'msg':'task not found!'}, HTTPStatus.NOT_FOUND

    current_app.db.session.delete(task)
    current_app.db.session.commit()

    return '', HTTPStatus.NO_CONTENT
