from core import db


class RoleMenu(db.Model):
    __tablename__ = 'lea_role_menu'
    roleId = db.Column("role_id", db.Integer, db.ForeignKey("lea_role.role_id"), primary_key=True,
                       comment="角色ID")
    menuId = db.Column("menu_id", db.Integer, db.ForeignKey("lea_menu.menu_id"), comment="菜单ID")
