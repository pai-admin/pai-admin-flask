from core import db


class RoleMenu(db.Model):
    __tablename__ = 'lea_role_menu'
    roleId = db.Column("role_id", db.Integer, primary_key=True, comment="角色ID")
    menuId = db.Column("menu_id", db.Integer, comment="菜单ID")
