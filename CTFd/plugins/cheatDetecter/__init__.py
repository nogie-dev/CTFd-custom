import hashlib
from CTFd.models import db

from CTFd.utils.user import (
    get_ip, 
    get_current_user,
    get_current_user_attrs
)
from CTFd.models import Flags
from .models import DynamicFlag

def insert_dynamic_flag(challenge_id, created_flag, flag_type):
    add_flag = Flags(
         challenge_id=challenge_id,
         type=flag_type if flag_type is not None else "static",
         content=created_flag,
         data=""
    )
    db.session.add(add_flag)
    db.session.commit()

def flag_created_log(container_id, chal_id, team_id, user_id):
        concat_str = str(container_id) + str("tmp")
        hashing_flag = hashlib.sha256(concat_str.encode()).hexdigest()
        add_log = DynamicFlag(
            created_flag=hashing_flag,
            container_id=container_id,
            challenge_id=chal_id,
            #team_id=safe_team_id,
            user_id=user_id,
            user_ip=get_ip()
        )
        flag_type=None
        insert_dynamic_flag(chal_id, hashing_flag, flag_type)

        db.session.add(add_log)
        db.session.commit()

def cheat_detecter(submission):
    user_id=get_current_user_attrs.id
    

def load(app):
    app.db.create_all()
        

