import datetime
from core import db


class DictType(db.Model):
    __tablename__ = 'lea_dict_type'
    typeId = db.Column("type_id", db.Integer, primary_key=True, comment="字典ID")
    parentId = db.Column("parent_id", db.Integer, comment="上级ID")
    typeName = db.Column("type_name", db.String(64), comment="字典名称")
    flag = db.Column(db.String(10), comment="字典编码")
    rank = db.Column(db.Integer, comment="排序")
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
