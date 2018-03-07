from app.Model.BaseUtilityF import (BaseEntity,
                                    Base)

from sqlalchemy import Column, Integer, String

class PublishInfoLablesModel(Base,BaseEntity):

    # 表名
    __tablename__ = 'publish_lables'

    # 记录publish_info 的 id
    publish_info_id = Column(Integer)

    # 记录publish_lables 的 id
    publish_lables_id = Column(Integer)

    def Create(self):
        return 0

    def Modify(self, KeyValue):
        return 0;

