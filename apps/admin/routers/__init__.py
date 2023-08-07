from flask import Blueprint

from . import account


def init_route(bp: Blueprint) -> None:
    # 获取验证码
    bp.add_url_rule("/get-code", methods=["GET"], endpoint="get-code", view_func=account.code)
    # 登录
    bp.add_url_rule("/login", methods=["POST"], endpoint="login", view_func=account.login)
    # 账号信息
    bp.add_url_rule("/info", methods=["GET"], endpoint="info", view_func=account.info)
    # 退出登录
    bp.add_url_rule("/logout", methods=["POST"], endpoint="logout", view_func=account.logout)
    # 修改密码
    bp.add_url_rule("/editPwd", methods=["POST"], endpoint="edit_pwd", view_func=account.login)
    # 菜单权限
    bp.add_url_rule("/auth", methods=["GET"], endpoint="auth", view_func=account.auth)
    # 修改资料
    bp.add_url_rule("/info/edit", methods=["POST"], endpoint="edit_info", view_func=account.login)
    # 个人日志
    bp.add_url_rule("/log/my", methods=["GET"], endpoint="my_log", view_func=account.login)
    # 日志列表
    bp.add_url_rule("/log/list", methods=["GET"], endpoint="get_log", view_func=account.get_log)
    # 删除日志
    bp.add_url_rule("/log/del", methods=["DELETE"], endpoint="del_log", view_func=account.login)
