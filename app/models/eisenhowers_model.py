from app.configs.database import db


class EisenhowerModel(db.Model):

    __tablename__ = "eisenhowers"

    id: int = db.Column(db.Integer, primary_key=True)
    type: str = db.Column(db.VARCHAR(200))

    tasks = db.relationship("TasksModel", backref="eisenhowers", uselist=False)
