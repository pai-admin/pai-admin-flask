import datetime
from core import db


class Account(db.Model):
    __tablename__ = 'lea_account'
    accountId = db.Column("account_id", db.Integer, primary_key=True, comment="账号ID")
    deptId = db.Column("dept_id", db.Integer, db.ForeignKey("lea_dept.dept_id"), comment="部门ID")
    avatar = db.Column(db.String(255), comment="头像")
    username = db.Column(db.String(30), comment="用户名")
    password = db.Column(db.String(100), comment="密码")
    salt = db.Column(db.String(6), comment="密码盐")
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
