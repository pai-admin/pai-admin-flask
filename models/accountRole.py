from core import db


class AccountRole(db.Model):
    __tablename__ = 'lea_account_role'
    accountId = db.Column("account_id", db.Integer, primary_key=True, comment="账号ID")
    roleId = db.Column("role_id", db.Integer, comment="角色ID")
