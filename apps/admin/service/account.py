from core import Response
from models import Account
from utils import Captcha, Tools
from core.redis import redis_client
from flask import current_app
from schemas import AccountSchema
from apps.admin.req import loginReq


# 获取验证码
def get_code():
    code, base64_data = Captcha.gen_base64()
    uuid = Tools.make_uuid()
    # 缓存下数据
    redis_client.set(current_app.config.get("TOKEN_KEY") + uuid, Tools.make_md5(str(code)), 300)
    return Response.success("success", {
        "verifyId": uuid,
        "base64Content": base64_data
    })


# 登录
def login(params: loginReq):
    # 验证码验证
    code = redis_client.get(current_app.config.get("TOKEN_KEY") + params["verifyId"])
    if code is None:
        return Response.fail("验证码不正确")
    # 取完就删除
    redis_client.delete(current_app.config.get("TOKEN_KEY") + params["verifyId"])
    if str(code, "utf-8") != Tools.make_md5(params["verifyCode"]):
        return Response.fail("验证码不正确")
    # 查询账号
    account = Account.query.filter_by(username=params['username'], del_flag=0).first()
    if not account:
        return Response.fail("用户名或者密码错误")
    if account.password != Tools.make_md5(params['password'] + account.salt):
        return Response.fail("用户名或者密码错误")
    if account.status != 1:
        return Response.fail("账号已被禁用")
    # 生成token
    token = Tools.make_token()
    redis_client.set(current_app.config.get("TOKEN_KEY") + token, Tools.model_to_json(AccountSchema, account),
                     current_app.config.get("TOKEN_TTL"))
    # 登录日志 和 操作权限
    return Response.success("success", {
        "token": token
    })
