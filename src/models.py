from config import db


class Task(db.Model):
    __tablename__ = 'tasks'
    ## TODO: Find if there's a sqlalchemy data type for UUIDs
    ## TODO: Is there a way to auto-generate UUIDs on the SQL-level?
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    is_complete = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Task {self.name}>"

    ## TODO: Find a library for a 'one-liner' way to serialize Model
    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "author": self.author,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_complete": self.is_complete
        }