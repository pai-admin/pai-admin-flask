import os
from flask import Flask, send_from_directory

from apps.admin.req import common
from config.config import Config
import apps.admin
from core import mysql, redis, error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def create_app() -> Flask:
    app = Flask(ROOT_DIR)
    # 初始化配置
    init_config(app)
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


def init_config(app):
    # 引入配置
    app.config['ROOT_PATH'] = ROOT_DIR
    app.config['RUNTIME_PATH'] = os.path.join(ROOT_DIR, "runtime")
    app.config['UPLOAD_PATH'] = os.path.join(ROOT_DIR, "upload")
    app.config['STATIC_PATH'] = os.path.join(ROOT_DIR, "static")
    app.config.from_object(Config)

    def static_file(filename):
        return send_from_directory(app.config['STATIC_PATH'], filename)

    def upload_file(filename):
        return send_from_directory(app.config['UPLOAD_PATH'], filename)

    # 静态文件目录
    app.add_url_rule("/static/<path:filename>", methods=["GET"], endpoint=None, view_func=static_file)
    app.add_url_rule("/upload/<path:filename>", methods=["GET"], endpoint=None, view_func=upload_file)
