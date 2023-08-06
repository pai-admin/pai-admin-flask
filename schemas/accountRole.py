from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import AccountRole


class AccountRoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccountRole
        include_fk = True
