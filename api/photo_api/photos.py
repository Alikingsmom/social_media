from api import app
from fastapi import Request, UploadFile, Body
from database.photoservice import change_photo_db


# get all photos or 1 photo and user id obyedenili 3 parametra
@app.get('/api/photo')
async def get_all_or_exact_photo(photo_id: int = 0, user_id: int = 0):
    pass


# izmenit photo profilya
@app.put('/api/photo')
async def change_user_photo(photo_id: int = Body(...), photo_file: UploadFile = Body(...)):

    if photo_file:
        # save photo in file
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}, jpg')

    return {'status': 1, 'message': 'photo successfully changed'}


# udalit photo
@app.delete('/api/photo')
async def delete_user_photo():
    pass
