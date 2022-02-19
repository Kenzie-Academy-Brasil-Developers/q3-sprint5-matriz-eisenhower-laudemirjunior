from flask import Blueprint
from app.controllers.delete_categories_controller import delete_category
from app.controllers.patch_categories_controller import patch_category
from app.controllers.post_categories_controller import post_category


bp = Blueprint("bp_categories", __name__, url_prefix="/categories")

bp.post("")(post_category)

bp.patch("/<id>")(patch_category)

bp.delete("/<id>")(delete_category)

