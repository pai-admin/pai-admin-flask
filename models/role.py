import datetime
from core import db


class Role(db.Model):
    __tablename__ = 'lea_role'
    roleId = db.Column("role_id", db.Integer, primary_key=True, comment="角色ID")
    roleName = db.Column("role_name", db.String(30), comment="角色名称")
    checkedMenus = db.Column("checked_menus", db.String(30), comment="选中的菜单(不包含半选，仅做数据展示用)")
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    flag = db.Column(db.String(20), comment="角色名称")
    rank = db.Column(db.Integer, comment="排序")
    remark = db.Column(db.String(255), comment="备注")
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
