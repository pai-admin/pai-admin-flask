from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import Dept


class DeptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dept
        include_fk = True
        exclude = ["del_flag"]
