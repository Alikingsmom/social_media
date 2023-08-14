from api import app


# poluchit neskolko heshtegov
@app.get('/api/hashtag')
async def get_some_hashtags(size: int = 20, page: int = 1):
    pass


@app.get('/api/hashtag/<str:hashtag_name>')
async def get_exact_hashtag(hashtag_name: str):
    pass