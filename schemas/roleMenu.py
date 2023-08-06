from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import RoleMenu


class RoleMenuSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleMenu
        include_fk = True
