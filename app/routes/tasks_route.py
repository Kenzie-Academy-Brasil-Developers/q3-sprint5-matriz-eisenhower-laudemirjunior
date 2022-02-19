from flask import Blueprint
from app.controllers.delete_tasks_controller import delete_tasks
from app.controllers.patch_tasks_controller import patch_tasks
from app.controllers.post_tasks_controller import post_task


bp = Blueprint("bp_tasks", __name__, url_prefix="/tasks")

bp.post("")(post_task)

bp.patch("/<id>")(patch_tasks)

bp.delete("/<id>")(delete_tasks)

