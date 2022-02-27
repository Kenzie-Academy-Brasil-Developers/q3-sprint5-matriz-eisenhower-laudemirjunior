from dataclasses import dataclass
from app.configs.database import db
from app.models.tasks_categories_table import tasks_categories


@dataclass
class CategoriesModel(db.Model):

    __tablename__ = "categories"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    description: str = db.Column(db.TEXT, default="")

    tasks = db.relationship(
        "TasksModel", secondary=tasks_categories, backref="categories"
    )
