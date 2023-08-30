from flask_marshmallow.sqla import SQLAlchemyAutoSchema, auto_field
from models import AccountLog


class AccountLogSchema(SQLAlchemyAutoSchema):
    createTime = auto_field(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AccountLog
        include_fk = True
