from flask import request, current_app
from core import Response
from plugins import storage


def upload():
    file = request.files.get("file")
    name, path, size = storage.local_upload(file, current_app)
    return Response.success("success", {
        "name": name,
        "path": path,
        "size": size
    })
