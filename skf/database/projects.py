from skf.database import db

class Project(db.Model):
    
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    version = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Text, nullable=False)
    design = db.Column(db.Boolean)

    def __init__(self, name, version, description, timestamp, design):
        self.name = name
        self.version = version
        self.description = description
        self.timestamp = timestamp
        self.design = design


