#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        # create 2 users

        # create 2 blogs (blogs won't belong to a user for this)

        # have both users comment on both blogs
