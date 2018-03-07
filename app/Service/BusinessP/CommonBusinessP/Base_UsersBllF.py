from sqlalchemy.sql.elements import and_

from app.Model.CommonModuleP.Base_UserF import UserModel
from sqlalchemy.orm import sessionmaker;

from app.Model.CommonModuleP.Base_UserF import UserModel;
from app.Service.BusinessP.BaseUtilityF import (baseBllManager)

from app.Service.RepositoryP.RepositoryF import Repository


# 用户的业务逻辑层
class Base_UserBll(Repository):
    '''
    user = UserModel(name = 'zhuge')
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/infoplatformdb', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session();
    session.add(user);
    # 提交保存
    session.commit();
    '''

    # 向处理函数中传入对象
    def CheckUser(self, mobile, password):
        session = baseBllManager.GetConn()();

        result = session.query(UserModel).filter(
            and_(UserModel.mobile == mobile,
                 UserModel.password == password)
        ).all()

        # 在这里提交了用户的修改，开始连接数据库，将修改
        # session.commit();
        # 关闭session
        session.close();

        # 查无此用户 返回false
        if len(result) is 0:
            return False;
        return True;
