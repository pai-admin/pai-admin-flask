from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import DictType


class DictTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DictType
        include_fk = True
        exclude = ["delFlag"]
