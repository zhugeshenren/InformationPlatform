import abc

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,DateTime,Boolean

# 使用 type 动态的创建了一个对象
Base = declarative_base();


# 定义所有实体的基本类型，所有的实体继承于此
class BaseEntity():

    @abc.abstractclassmethod
    def Create(self):
        '''
        :return: 不返回,是一个方法
        '''

    @abc.abstractclassmethod
    def Modify(self,KeyValue):
        '''
        修改类
        :param KeyValue: 参数
        :return:
        '''

    # 创建时间
    create_time = Column(DateTime);

    # 更新时间
    update_time = Column(DateTime);

    # 创建者 约定 CreatePerson为0时表示当前用户
    create_person = Column(Integer)

    # 更新人
    update_person = Column(Integer)

    # 数据状态标记
    state = Column(Boolean)