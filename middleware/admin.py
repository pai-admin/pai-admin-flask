import json
from functools import wraps
from flask import request, current_app, jsonify
from core import redis_client, Response, db
from models import AccountLog
from utils import Tools


def AdminAuth(name="", auth="*", needLogin=True, needAuth=True):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # 无需登录
            if not needLogin:
                return func(*args, **kwargs)
            token = request.headers.get('Authorization')
            if token is None:
                return Response.response(Tools.CODE_INVALID, "登录失效")
            _str = redis_client.get(current_app.config.get("TOKEN_KEY") + token)
            if _str is None:
                return Response.response(Tools.CODE_INVALID, "登录失效")
            dic = json.loads(str(_str, "utf-8"))
            if not dic:
                return Response.response(Tools.CODE_INVALID, "登录失效")
            # 续签token
            redis_client.set(current_app.config.get("TOKEN_KEY") + token, _str,
                             current_app.config.get("TOKEN_TTL"))
            # 无需权限
            if not needAuth or auth == "*":
                return func(*args, **kwargs)
            # 鉴权
            _arr = redis_client.get(current_app.config.get("TOKEN_KEY") + "AUTH:" + str(dic['accountId']))
            if not _arr:
                return Response.response(Tools.CODE_INVALID, "权限不足-1")
            arr = json.loads(_arr)
            if (request.method + ":" + auth).lower() not in arr:
                return Response.response(Tools.CODE_INVALID, "权限不足-2")
            result = func(*args, **kwargs)
            # 日志记录
            log = AccountLog(
                accountId=dic['accountId'],
                username=dic['username'],
                title=name,
                method=request.method,
                flag=auth,
                code=200,
                ip=request.remote_addr,
                ua=request.user_agent,
                request=json.dumps(request.values.to_dict(), ensure_ascii=False),
                response=json.dumps(result, ensure_ascii=False)
            )
            db.session.add(log)
            db.session.commit()
            return result

        return inner

    return decorator
