from database import get_db
from database.models import PostPhoto


# get all or exact photo
def get_all_or_exact_photo_db(photo_id, user_id):
    db = next(get_db())

    # if we need all photos of user
    if user_id:
        exact_user_photos = db.query(PostPhoto).filter_by(user_id).all()

        return {'status': 1, 'message': exact_user_photos}

    # if we need exact photo
    elif photo_id:
        exact_photo = db.query(PostPhoto).filter_by(user_id).first()

        return {'status': 1, 'message': exact_photo}

    else:
        all_photos = db.query(PostPhoto).all()

        return {'status': 1, 'message': all_photos}


# change profile photo
def change_photo_db(photo_id, new_photo_path):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        exact_photo = db.query()
        db.commit()

        return True

    return False


def delete_photo_db(photo_id):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        db.delete(exact_photo)
        db.commit()

        return 'Photo deleted'

    return 'photo not found'

