import json

from core import Response, db
from models import Account, Menu, RoleMenu, AccountRole, Dept, Role
from utils import Captcha, Tools
from core.redis import redis_client
from flask import current_app, request
from schemas import AccountSchema
from apps.admin.req import loginReq
from models import AccountLog


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
    account = Account.query.filter_by(username=params['username'], delFlag=0).first()
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
    # 登录日志
    log = AccountLog(
        accountId=account.accountId,
        username=account.username,
        title="用户登录",
        method="post",
        flag="admin:login",
        code=200,
        ip=request.remote_addr,
        ua=request.user_agent
    )
    # 添加不成功就会自动抛异常
    db.session.add(log)
    db.session.commit()
    # 缓存操作权限
    apis = db.session.query(Menu).join(RoleMenu, Menu.menuId == RoleMenu.menuId).join(
        AccountRole, RoleMenu.roleId == AccountRole.roleId).filter(
        AccountRole.accountId == account.accountId, Menu.delFlag == 0, Menu.type == 2).with_entities(
        Menu.method + ":" + Menu.flag).distinct().all()
    if apis:
        _arr = []
        for api in apis:
            _arr.append(api[0])
        redis_client.set(current_app.config.get("TOKEN_KEY") + "AUTH:" + str(account.accountId),
                         json.dumps(_arr, ensure_ascii=False))
    # 登录成功
    return Response.success("success", {
        "token": token
    })


# 个人信息
def info(accountId):
    account, dept = db.session.query(Account, Dept).join(Dept, Account.deptId == Dept.deptId).filter(
        Account.accountId == accountId, Account.delFlag == 0).first()
    return Response.success("success", {
        "accountId": account.accountId,
        "username": account.username,
        "avatar": account.avatar,
        "deptName": dept.deptName,
    })


# 获取菜单权限
def get_auth(accountId):
    # 按钮权限
    result = db.session.query(AccountRole, RoleMenu, Menu).join(RoleMenu, AccountRole.roleId == RoleMenu.roleId).join(
        Menu, RoleMenu.menuId == Menu.menuId).filter(AccountRole.accountId == accountId, Menu.delFlag == 0,
                                                     Menu.type == 1).order_by(
        Menu.rank.desc()).with_entities(Menu.flag).distinct().all()
    buttons = []
    for i in result:
        buttons += list(i)
    # 角色权限
    result = db.session.query(AccountRole, Role).join(Role, AccountRole.roleId == Role.roleId).filter(
        AccountRole.accountId == accountId, Role.delFlag == 0).with_entities(Role.flag).distinct().all()
    roles = []
    for i in result:
        roles += list(i)
    # 菜单权限
    result = db.session.query(AccountRole, RoleMenu, Menu).join(RoleMenu, AccountRole.roleId == RoleMenu.roleId).join(
        Menu, RoleMenu.menuId == Menu.menuId).filter(AccountRole.accountId == accountId, Menu.delFlag == 0,
                                                     Menu.type == 0).order_by(
        Menu.rank.desc()).distinct().all()
    menus = []
    for accountRole, roleMenu, menu in result:
        menus.append({
            "menuId": menu.menuId,
            "parentId": menu.parentId,
            "title": menu.title,
            "name": menu.name,
            "path": menu.path,
            "icon": menu.icon,
            "hidden": menu.hidden
        })
    return Response.success("菜单权限", {
        "buttons": buttons,
        "roles": roles,
        "menus": menus
    })


def logout():
    token = request.headers.get('Authorization')
    redis_client.delete(current_app.config.get("TOKEN_KEY") + token)
    return Response.success("退出成功")


def get_log(params):
    print(params)
    return Response.success("qeq", [])
