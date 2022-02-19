from flask import Blueprint
from app.controllers.get_all_controller import get_all


bp = Blueprint("bp_simple_route", __name__, url_prefix="/")

bp.get("")(get_all)

