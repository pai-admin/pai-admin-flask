from pre_request import Rule

# 登录
loginReq = {
    "username": Rule(type=str, required=True, gte=3, lte=20, trim=True),
    "password": Rule(type=str, required=True, len=32, trim=True),
    "verifyCode": Rule(type=str, required=True),
    "verifyId": Rule(type=str, required=True)
}
