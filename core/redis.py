from flask import Flask
from flask_redis import FlaskRedis

redis_client = FlaskRedis()


def init_redis(app: Flask):
    redis_client.init_app(app)
