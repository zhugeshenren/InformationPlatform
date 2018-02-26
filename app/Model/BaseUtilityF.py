import abc

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,DateTime,Boolean



# 使用 type 动态的创建了一个对象

Base = declarative_base();

'''
    BaseEntity 定义所有实体的基本类型，所有的实体继承于此

    返回给前端的数据格式
    (1) List[tuple,tuple,.....]
        第一个tuple标识列属性，其余的tuple存储信息
    (2) 使用List[dict,dict,....]
        格式化之后为json数据可以直接读取
'''

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

    # 利用反射 将类转化为字典
    def ToDict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


    # 用户id
    id = Column(Integer, primary_key=True)

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