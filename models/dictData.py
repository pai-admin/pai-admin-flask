import datetime
from core import db


class DictData(db.Model):
    __tablename__ = 'lea_dict_data'
    dataId = db.Column("data_id", db.Integer, primary_key=True, comment="字典ID")
    typeId = db.Column("type_id", db.Integer, db.ForeignKey("lea_dict_type.role_id"), comment="上级ID")
    name = db.Column(db.String(20), comment="项名称")
    content = db.Column(db.String(255), comment="键值")
    rank = db.Column(db.Integer, comment="排序")
    status = db.Column(db.Integer, comment="状态")
    delFlag = db.Column("del_flag", db.Integer, comment="状态(1删除,0关闭)")
    createTime = db.Column("create_time", db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updateTime = db.Column("update_time", db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                           comment='更新时间')
