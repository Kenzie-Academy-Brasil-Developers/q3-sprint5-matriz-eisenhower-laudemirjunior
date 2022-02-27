from flask import current_app
from app.models.categories_model import CategoriesModel


def data_categories_to_patch(data):

    if "categories" in data.keys():
        category_list = data.pop("categories")
        data["categories"] = []

        for category in category_list:
            category = category.lower()

            category_query = CategoriesModel.query.filter_by(
                name=category
            ).one_or_none()

            if not category_query:
                category_query = CategoriesModel(**{"name": category})

                current_app.db.session.add(category_query)
                current_app.db.session.commit()

            data["categories"].append(category_query)

    return data
