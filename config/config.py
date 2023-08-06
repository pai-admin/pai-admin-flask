import logging
import os


class Config:
    # 应用名称
    APP_NAME = os.getenv("APP_NAME", "pai-admin")
    # 版本
    VERSION = os.getenv("VERSION", "1.0.1")
    # 数据库连接字符串
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # 默认日志等级
    LOG_LEVEL = logging.WARN
    # debug
    DEBUG = os.getenv("DEBUG") == "true"
    # redis配置
    REDIS_URL = os.getenv("REDIS_URL")
    # 是否显示SQL
    SQLALCHEMY_ECHO = DEBUG
