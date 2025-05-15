from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from CTFd.models import db
from CTFd.models import Challenges


class DynamicFlag(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )

    created_flag = db.Column(db.Text)
    container_id = db.Column(db.Text)
    challenge_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer)
    user_ip = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(DynamicFlag, self).__init__(**kwargs)