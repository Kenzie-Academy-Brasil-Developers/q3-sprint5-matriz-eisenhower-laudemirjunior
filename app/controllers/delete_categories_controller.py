from http import HTTPStatus
from flask import current_app
from app.models.categories_model import CategoriesModel


def delete_category(id):
    category: CategoriesModel = CategoriesModel.query.get(id)

    if not category:
        return {'msg':'category not found!'}, HTTPStatus.NOT_FOUND

    current_app.db.session.delete(category)
    current_app.db.session.commit()

    return {}, HTTPStatus.NO_CONTENT