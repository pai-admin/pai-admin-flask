import datetime
import os.path
import time
from flask import current_app
from werkzeug.datastructures.file_storage import FileStorage
from utils import Tools


def local_upload(file: FileStorage, app: current_app):
    root_path = app.config.get("ROOT_PATH")
    today = datetime.datetime.today()
    path = os.path.join("upload", str(today.year), str(today.month), str(today.day))
    filename = file.filename
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    file_name = Tools.make_md5(str(time.time()) + Tools.random_str(6)) + "." + ext
    file_path = os.path.join(root_path, path, file_name)
    if not os.path.exists(path):
        os.makedirs(path)
    file.save(file_path)
    return file_name, os.path.join(path, file_name), os.path.getsize(file_path)
