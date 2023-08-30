from flask import send_from_directory, current_app
from apps.admin.service import common
from middleware import AdminAuth


@AdminAuth(name="文件上传", needLogin=False)
def upload():
    return common.upload()
