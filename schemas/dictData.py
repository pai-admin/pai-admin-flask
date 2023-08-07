from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import DictData


class DictDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DictData
        include_fk = True
        exclude = ["delFlag"]
