from flask import Blueprint

from . import account


def init_route(bp: Blueprint) -> None:
    # 获取验证码
    bp.add_url_rule("/get-code", methods=["GET"], endpoint="get-code", view_func=account.code)
    # 登录
    bp.add_url_rule("/login", methods=["POST"], endpoint="login", view_func=account.login)
