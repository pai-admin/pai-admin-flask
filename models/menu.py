import datetime
from core import db


class Menu(db.Model):
    __tablename__ = 'lea_menu'
    menuId = db.Column("menu_id", db.Integer, primary_key=True, comment="菜单ID")
    parentId = db.Column("parent_id", db.Integer, comment="上级ID")
    title = db.Column(db.String(30), comment="菜单名称")
    type = db.Column(db.Integer, comment="0菜单 1按钮 2接口")
    method = db.Column(db.String(10), comment="请求方式")
    flag = db.Column(db.String(255), comment="接口或按钮标识")
    name = db.Column(db.String(64), comment="页面名称")
    path = db.Column(db.String(255), comment="页面路径")
    icon = db.Column(db.String(50), comment="菜单icon")
    rank = db.Column(db.Integer, comment="排序")
    hidden = db.Column(db.Integer, comment="隐藏路由")
    remark = db.Column(db.String(255), comment="备注")
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
