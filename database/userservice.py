from database.models import User
from datetime import datetime

from database import get_db


#  user registration
def register_user_db(name, email, phone_number, password, user_city):
    db = next(get_db())

    # creating new user class
    new_user = User(name=name, email=email, phone_number=phone_number,
                    password=password, user_city=user_city, reg_date=datetime.now())

    # adding new user to db
    db.add(new_user)
    # save to db
    db.commit()

    return new_user.id


# check if user exists in users of database
def check_user_data_db(phone_number, email):
    db = next(get_db())

    # checking if exists in db
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()

    # if exist user
    if checker:
        return False

    # if no user
    return True


# check user's password
def check_user_password_db(email, password):
    db = next(get_db())

    # try to find user
    checker = db.query(User).filter_by(email=email).first()

    # if found same email check correctness of password
    if checker:
        # start comparing password
        if checker.password == password:
            return checker.id

        else:
            return 'wrong password'

    # if not found same email
    return 'wrong mail address'


# get info about user
def profile_info_db(user_id):
    db = next(get_db())

    # search user through id
    exact_user = db.query(User).filter_by(id=user_id).first()

    # if found user send all info about user
    if exact_user:
        return exact_user.email, \
            exact_user.phone_number, \
            exact_user.id, exact_user.name, \
            exact_user.reg_date, exact_user.user_city

    return 'User not found'


# change user data by user
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())

    # find user
    exact_user = db.query(User).filter_by(id=user_id).first()

    # check which info user wants to change
    if change_info == 'email':
        exact_user.email = new_data

    elif change_info == 'number':
        exact_user.phone_number = new_data

    elif change_info == 'name':
        exact_user.name = new_data

    elif change_info == 'city':
        exact_user.user_city = new_data

    elif change_info == 'password':
        exact_user.password = new_data

        # save changes in db
        db.commit()

        return 'Your info successfully changed'


    # if not found user in db
    return 'User not found'
