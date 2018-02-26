from app.Model.BaseUtilityF import (BaseEntity,
                                    Base)

from sqlalchemy import Column, Integer, String


class PublishInfoModel(BaseEntity,Base):
    # 表名
    __tablename__ = 'publish_info'

    # 标题
    title = String();

    # 描述1
    desc_one = String();

    # 描述2
    desc_two = String();

    # 描述3
    desc_three = String();

    # 描述缩略图的路径
    thumbnail = String();

    def Create(self):
        return 0

    def Modify(self, KeyValue):
        return 0;


