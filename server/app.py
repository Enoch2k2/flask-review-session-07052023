#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, Blog, Comment

# Views go here!


class Home(Resource):
    def get(self):
        return {'message': 'this works'}, 200


api.add_resource(Home, "/", endpoint='home')


class Blog(Resource):
    def get(self):
        return {'message': 'return json here that displays all the blogs, but also includes the blogs comments, each comment should also include the user'}, 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
