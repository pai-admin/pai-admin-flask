from core import db


class AccountRole(db.Model):
    __tablename__ = 'lea_account_role'
    accountId = db.Column("account_id", db.Integer, db.ForeignKey("lea_account.account_id"), primary_key=True,
                          comment="账号ID")
    roleId = db.Column("role_id", db.Integer, db.ForeignKey("lea_role.role_id"), comment="角色ID")
