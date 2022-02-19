from http import HTTPStatus
from app.models.categories_model import CategoriesModel 
from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError

def patch_category(id):
    try:
        data = request.get_json()
        category: CategoriesModel = CategoriesModel.query.get(id)

        if not category:
            return jsonify(msg='category not found!'), HTTPStatus.NOT_FOUND

        for key, value in data.items():
            setattr(category, key, value.lower())

        current_app.db.session.add(category)
        current_app.db.session.commit()

        return jsonify(category), HTTPStatus.OK

    except IntegrityError:
        return jsonify({"msg": "the name entered already exists in another record in the database!"})
