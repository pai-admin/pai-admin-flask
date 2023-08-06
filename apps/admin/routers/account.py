from apps.admin.service import account
from middleware import AdminAuth
from pre_request import pre
from apps.admin import req


@AdminAuth(name="用户登录", needLogin=False)
def login():
    # 接收并校验参数
    params = pre.parse(rule=req.loginReq)
    return account.login(params)


@AdminAuth(name="验证码", needLogin=False)
def code():
    return account.get_code()
