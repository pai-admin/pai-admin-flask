from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from models import Account


class AccountSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        include_fk = True
        exclude = ["delFlag", "salt", "password"]
