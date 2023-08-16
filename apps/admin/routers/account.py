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
    ac = Tools.get_account(request, current_app)
    return account.info(ac.accountId)


@AdminAuth(name="菜单权限", needAuth=False)
def auth():
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


@AdminAuth(name="修改信息", needAuth=False)
@pre.catch(post=req.editInfoReq)
def edit_info(params):
    ac = Tools.get_account(request, current_app)
    return account.edit_info(ac.accountId, params)


@AdminAuth(name="修改密码", needAuth=False)
@pre.catch(post=req.editPwdReq)
def edit_pwd(params):
    ac = Tools.get_account(request, current_app)
    return account.edit_pwd(ac.accountId, params)


@AdminAuth(name="修改密码", needAuth=False)
def my_log():
    ac = Tools.get_account(request, current_app)
    return account.my_log(ac.accountId)
