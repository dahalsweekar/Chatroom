from sqlalchemy.orm import Session
from . import schemas, model
from werkzeug.security import generate_password_hash


def register_user(db: Session, user: schemas.RegisterModel):
    db_user = model.User(firstname=user.firstname,
                         lastname=user.lastname,
                         email=user.email,
                         phone=user.phone,
                         password=generate_password_hash(user.password)
                         )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email):
    db_user = db.query(model.User).filter(model.User.email == email).first()
    return db_user


def get_all_info(db: Session):
    data = db.query(model.User).all()
    return data
