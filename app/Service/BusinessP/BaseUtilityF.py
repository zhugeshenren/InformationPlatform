# 公共的业务类
from sqlalchemy.orm import sessionmaker;
from sqlalchemy import create_engine


class BaseBllManager(object):
    _instance = None


    # 创建一个全局的连接池
    # 考虑异步并发执行时的锁的问题
    SqlSession = None;
    def SetConn(self,ConnStr):
        engine = create_engine(ConnStr, echo=False)
        self.SqlSession = sessionmaker(bind=engine)

    def GetConn(self):
        return self.SqlSession

    # 使用 __new__ 实现单例模型
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BaseBllManager,cls).__new__(cls,*args,**kwargs);
        return cls._instance;
