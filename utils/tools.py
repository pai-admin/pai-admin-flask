import hashlib
import json
import random
import string
import time
import uuid
from flask import request, current_app
from core import redis_client
from core.mysql import ma
from models import Account


class Tools(object):
    CODE_SUCCESS = 200
    CODE_FAIL = 400
    CODE_ERROR = 500
    CODE_INVALID = 401
    CODE_NO_AUTH = 403

    @classmethod
    def random_str(cls, num: int) -> str:
        arr = list(string.ascii_letters)
        arr.extend(map(str, list(range(0, 10))))
        return "".join(random.sample(arr, num))

    @classmethod
    def make_uuid(cls) -> str:
        return str(uuid.uuid1()).replace("-", "")

    @classmethod
    def make_md5(cls, data: str) -> str:
        hl = hashlib.md5()
        hl.update(data.encode("utf-8"))
        return hl.hexdigest()

    @classmethod
    def make_token(cls) -> str:
        return cls.make_uuid() + str(int(time.time())) + cls.random_str(8)

    @classmethod
    def model_to_dict(cls, schema: ma.Schema, data):
        return schema(many=isinstance(data, list)).dump(data)

    @classmethod
    def model_to_json(cls, schema: ma.Schema, data):
        common_schema = schema(many=isinstance(data, list))
        output = common_schema.dump(data)
        return json.dumps(output, ensure_ascii=False)

    @classmethod
    def get_account(cls, req: request, ca: current_app):
        token = req.headers.get('Authorization')
        if not token:
            return None
        _str = redis_client.get(ca.config.get("TOKEN_KEY") + token)
        if _str is None:
            return None
        dic = json.loads(str(_str, "utf-8"))
        return Account(accountId=dic["accountId"], username=dic['username'])
