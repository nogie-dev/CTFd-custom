from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from CTFd.models import db
from CTFd.models import Challenges

class DynamicFlag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)

    created_flag = db.Column(db.String(512))
    container_id = db.Column(db.String(512))
    challenge_id = db.Column(
        db.Integer, db.ForeignKey("challenges.id", ondelete="CASCADE")
    )
    team_id = db.Column(
        db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE")
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE")
    )
    user_ip = db.Column(db.String(64))

