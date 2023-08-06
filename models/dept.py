import datetime
from core import db


class Dept(db.Model):
    __tablename__ = 'lea_dept'
    deptId = db.Column("dept_id", db.Integer, primary_key=True, comment="部门ID")
    parentId = db.Column("parent_id", db.Integer, comment="上级ID")
    deptName = db.Column("dept_name", db.String(64), comment="部门名称")
    rank = db.Column(db.Integer, comment="排序")
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    remark = db.Column(db.String(255), comment="备注")
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
