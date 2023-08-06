import os
from flask import Flask
from config.config import Config
import apps.admin
from core import mysql, redis, error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def create_app() -> Flask:
    app = Flask(ROOT_DIR)
    # 引入配置
    app.config.from_object(Config)
    # 初始化数据库
    mysql.init_db(app)
    # 初始化缓存
    redis.init_redis(app)
    # 1. 先注册模块
    init_module(app)
    # 2. 再注册蓝图
    init_blueprint(app)
    # 3. 全局异常捕获
    error.init_error(app)
    return app


def init_blueprint(app):
    # 蓝图
    app.register_blueprint(admin.bp)


def init_module(app):
    # 注册admin模块
    admin.init_modules(app)
