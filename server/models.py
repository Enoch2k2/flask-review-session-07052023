from sqlalchemy_serializer import SerializerMixin

from config import db

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'


class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)

    def __repr__(self):
        return f'Blog ID: {self.id} title: {self.title} content: {self.content}'


class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    def __repr__(self):
        return f'Comment ID: {self.id} content: {self.content}'
