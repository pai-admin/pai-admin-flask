from pre_request import Rule

# 登录
loginReq = {
    "username": Rule(type=str, required=True, gte=3, lte=20, trim=True),
    "password": Rule(type=str, required=True, len=32, trim=True),
    "verifyCode": Rule(type=str, required=True),
    "verifyId": Rule(type=str, required=True)
}

# 查看日志
logReq = {
    "page": Rule(type=int, required=True),
    "limit": Rule(type=int, required=True),
    "startTime": Rule(type=str, required=False, location=["args"]),
    "endTime": Rule(type=str, required=False, location=["args"]),
    "title": Rule(type=str, required=False, location=["args"])
}

# 修改信息
editInfoReq = {
    "avatar": Rule(type=str, required=False),
}

# 修改密码
editPwdReq = {
    "oldPassword": Rule(type=str, required=False),
    "newPassword": Rule(type=str, required=False),
}

# 个人日志
myLogReq = {
    "page": Rule(type=int, required=True),
    "limit": Rule(type=int, required=True),
}
