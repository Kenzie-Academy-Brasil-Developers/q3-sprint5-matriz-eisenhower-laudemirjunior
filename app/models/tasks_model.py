from app.configs.database import db
from dataclasses import dataclass


@dataclass
class TasksModel(db.Model):
    
    __tablename__ = "tasks"
    
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.VARCHAR(100), nullable=True, unique=True)
    description: str = db.Column(db.Text)
    duration: int = db.Column(db.Integer)
    importance: int = db.Column(db.Integer)
    urgency: int = db.Column(db.Integer)
    
    eisenhower_id = db.Column(db.Integer, db.ForeignKey('eisenhowers.id'), nullable=False)

