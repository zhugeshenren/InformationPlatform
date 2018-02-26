from app.Model.BaseUtilityF import (BaseEntity,Base)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class PublishLablesModel(Base,BaseEntity):

    # 表名
    __tablename__ = 'publish_lables';

    # lable名称
    name = Column(String)

    # 描述
    desc_one = Column(String);

    def Create(self):
        return 0

    def Modify(self, KeyValue):
        return 0;

