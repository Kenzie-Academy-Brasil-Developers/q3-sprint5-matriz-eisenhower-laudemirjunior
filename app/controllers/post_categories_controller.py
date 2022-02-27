from flask import current_app, request, jsonify
from sqlalchemy.orm import Session
import sqlalchemy.exc
from app.models.categories_model import CategoriesModel
from http import HTTPStatus


def post_category():
    session: Session = current_app.db.session
    data = request.get_json()

    for value in data:
        data[value] = data[value].lower()

    try:
        new_category = CategoriesModel(**data)
        session.add(new_category)
        session.commit()
        return jsonify(new_category), HTTPStatus.CREATED

    except TypeError as error:
        return jsonify(error=str(error))

    except sqlalchemy.exc.IntegrityError as error:
        if "(psycopg2.errors.UniqueViolation)" in str(error):
            return jsonify(msg="category already exists!"), HTTPStatus.CONFLICT
