from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import Role


class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk = True
        exclude = ["del_flag"]
