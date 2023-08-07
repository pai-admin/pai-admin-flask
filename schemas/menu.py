from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import Menu


class MenuSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        include_fk = True
        exclude = ["delFlag"]
