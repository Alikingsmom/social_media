from api import app
from fastapi import Request
from database.postservice import get_all_or_exact_post_db, \
delete_exact_post_db



@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):

    post = get_all_or_exact_post(post_id)

    if post:
        exact_user_post = get_all_or_exact_post_db(post_id)

        return {'status': 1, 'message': exact_user_post}

    return {'status': 0, 'message': 'Wrong input'}


# izmenit post
@app.put('/api/post')
async def change_user_post(request: Request):

    data = await request.json()

    post_id = data.get('post_id')
    new_post = data.get('new_post')

    if post_id and new_post:
        change_post = change_post_text_db(post_id)
        return {'status': 1, 'message': 'Wrong input'}

    return {'status': 0, 'message': 'Wrong input'}


# udalit post
@app.delete('/api/post')
async def delete_user_post(request: Request):

    data = await request.json()

    post_id = data.get('post_id')

    if post_id:
        delete_post = delete_exact_post_db(post_id)
        return {'status': 1, 'message': delete_post}

    return {'status': 0, 'message': 'Wrong input'}

