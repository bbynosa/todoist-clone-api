from config import db


class Task(db.Model):
    __tablename__ = 'tasks'
    ## TODO: Find if there's a sqlalchemy data type for UUIDs
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    priority = db.Column(db.String(30), nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    created_by = db.Column(db.String(50), nullable=False)
    assigned_to = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Task {self.name}>"

    ## TODO: Find a library for a 'one-liner' way to serialize Model
    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "priority": self.priority,
            "notes": self.notes,
            "created_by": self.created_by,
            "assigned_to": self.assigned_to,
        }