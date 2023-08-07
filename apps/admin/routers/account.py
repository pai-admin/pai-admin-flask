from apps.admin.service import account
from middleware import AdminAuth
from pre_request import pre
from apps.admin import req
from flask import request, current_app
from utils import Tools


@AdminAuth(name="用户登录", needLogin=False)
@pre.catch(post=req.loginReq)
def login(params):
    return account.login(params)


@AdminAuth(name="验证码", needLogin=False)
def code():
    return account.get_code()


@AdminAuth(name="账号信息", needAuth=False)
def info():
    # 获取登录信息
    ac = Tools.get_account(request, current_app)
    return account.info(ac.accountId)


@AdminAuth(name="菜单权限", needAuth=False)
def auth():
    # 获取登录信息
    ac = Tools.get_account(request, current_app)
    return account.get_auth(ac.accountId)


@AdminAuth(name="退出登录", needAuth=False)
def logout():
    # 退出登录
    return account.logout()


@AdminAuth(name="查看日志", auth="admin:log:list")
@pre.catch(get=req.logReq)
def get_log(params):
    return account.get_log(params)
