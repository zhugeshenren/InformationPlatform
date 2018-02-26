from app.Model.BaseUtilityF import (BaseEntity,
                                    Base)

from sqlalchemy import Column, Integer, String

# DR

class UserModel(Base,BaseEntity):
    # 表名
    __tablename__ = 'users'

    # 姓名
    name = Column(String)

    # 密码
    password = Column(String)

    # 手机
    mobile = Column(String)

    # 所属区域id
    field_id = Column(Integer)

    # 详细记录ID
    record_id = Column(Integer)

    def Create(self):
        return 0

    def Modify(self,KeyValue):
        return 0
