from api import app
from fastapi import Request
from database.postservice import get_exact_post_comments_db, \
    public_comment_db, change_comment_text_db, delete_exact_comment_db

# Получить коментарии определенного паста
@app.get('/api/comment')
async def get_exact_post_comments(request: Request):
    # Получить JSON со всеми данными которые пришли из front
    data = await request.json()

    # Получить ключь post_id из data
    post_id = data.get('post_id')


    if post_id:
        # Получаем данные из базы
        exact_post_comment = get_exact_post_comments_db(post_id)


        return {'status': 1, 'message': exact_post_comment}

    return {'status': 0, 'message': 'Неверный ввод данных'}

# опубликовать комментарий к посту
@app.post("/api/comment")
async def public_comment(request: Request):
    data = await request.json()
    post_id = data.get("post_id")
    user_id = data.get("user_id")
    text = data.get("text")
    reg_date = data.get("reg_date")
    if post_id and user_id and text and reg_date:
        public_comment_db(post_id, user_id, text, reg_date)
        return {"status": 1, "message": "успешно опубликовано"}
    return {"status": 0, "message": "ошибка"}

# изменить комментарий
@app.put("/api/comment")
async def change_exact_user_comment(request: Request):
    data = await request.json()
    comment_id = data.get("comment_id")
    new_comment_text = data.get("new_comment_text")
    if comment_id and new_comment_text:
        change_comment_text_db(comment_id, new_comment_text)
        return {"status": 1, "message": "успешно изменено"}
    return {"status": 0, "message": "ошибка"}

# удалить комментарий
@app.delete("/api/comment")
async def delete_exact_user_comment(request: Request):
    data = await request.json()
    comment_id = data.get("comment_id")
    if comment_id:
        delete_exact_comment_db(comment_id)
        return {"status": 1, "message": "успешно удалено"}
    return {"status": 0, "message": "ошибка"}