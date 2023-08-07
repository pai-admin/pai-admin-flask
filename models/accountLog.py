import datetime
from core import db


class AccountLog(db.Model):
    __tablename__ = 'lea_account_log'
    logId = db.Column("log_id", db.Integer, primary_key=True, comment="日志ID")
    accountId = db.Column("account_id", db.Integer, db.ForeignKey("lea_account.account_id"), comment="账号ID")
    username = db.Column(db.String(30), comment="管理员名称")
    title = db.Column(db.String(50), comment="操作名称")
    method = db.Column(db.String(10), comment="请求方式")
    flag = db.Column(db.String(30), comment="权限标识")
    code = db.Column(db.Integer, comment='状态 200成功 400失败 500错误')
    request = db.Column(db.Text, comment="请求")
    response = db.Column(db.Text, comment="响应")
    ip = db.Column(db.String(50), comment="IP")
    ua = db.Column(db.String(500), comment="浏览器")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
