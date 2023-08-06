from utils import Tools
from flask import jsonify


class Response(object):
    @classmethod
    def response(cls, code=200, msg="ok", data=None, count=None):
        _r = {
            "code": code,
            "msg": msg
        }
        if data is not None:
            _r["data"] = data
        if count is not None:
            _r["count"] = count
        return jsonify(_r)

    @classmethod
    def success(cls, msg, data=None, count=None):
        return cls.response(Tools.CODE_SUCCESS, msg, data, count)

    @classmethod
    def fail(cls, msg, data=None, count=None):
        return cls.response(Tools.CODE_FAIL, msg, data, count)

    @classmethod
    def error(cls, msg, data=None):
        return cls.response(Tools.CODE_ERROR, msg, data)
