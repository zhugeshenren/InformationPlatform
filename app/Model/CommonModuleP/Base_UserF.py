from app.Model.BaseUtilityF import BaseEntity
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 使用 type 动态的创建了一个对象
Base = declarative_base();

class UserModel(Base,BaseEntity):

    # 表名
    __tablename__ = 'users'

    # 用户id
    id = Column(Integer,primary_key=True)

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
        return 0;



