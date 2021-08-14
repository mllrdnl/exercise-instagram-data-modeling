import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, index=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Followers(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class MediaType(enum.Enum):
    PICTURE = "PICTURE"
    VIDEO = 'VIDEO'

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship(Post)
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e