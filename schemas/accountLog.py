from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import AccountLog


class AccountLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccountLog
        include_fk = True
