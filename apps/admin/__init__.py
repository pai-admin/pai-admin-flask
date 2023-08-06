from flask import Flask, Blueprint
from config.admin import Admin as AdminConfig
from apps.admin.routers import init_route

bp = Blueprint('admin', __name__, url_prefix='/admin')


def init_modules(app: Flask) -> None:
    # 导入配置
    app.config.from_object(AdminConfig)
    # 路由注册
    init_route(bp)
