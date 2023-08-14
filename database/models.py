from sqlalchemy import Column, DateTime, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# users table
class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    user_city = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    password = Column(String)

    reg_date = Column(DateTime)


# posts table
class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


# photos table
class PostPhoto(Base):
    __tablename__ =  'post_photos'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('user_posts.id'))
    photo_path = Column(String, nullable=False)

    post_fk = relationship(UserPost, lazy='subquery')


# hashtags table
class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, nullable=False, unique=True)
    post_id = Column(BigInteger, ForeignKey('user_posts.id'))

    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')


# comments table
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey('user_posts.id'))
    user_id = Column(BigInteger, ForeignKey('users.id'))
    main_text = Column(String, nullable=True, unique=True)

    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')
    user_fk = relationship(User, lazy='subquery')
