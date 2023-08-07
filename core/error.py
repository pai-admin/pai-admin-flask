from sqlalchemy.exc import SQLAlchemyError
from core.response import Response
from pre_request.exception import ParamsValueError


def init_error(app):
    @app.errorhandler(ParamsValueError)
    def param_error(e):
        return Response.fail(e.message), 200

    @app.errorhandler(404)
    def no_found_error(e):
        return Response.fail("路由不存在"), 200

    @app.errorhandler(SQLAlchemyError)
    def sql_error(e):
        return Response.fail(e._message()), 200
