from sqlalchemy.sql.elements import and_

from app.Model.CommonModuleP.Base_UserF import UserModel
from sqlalchemy.orm import sessionmaker;

from app.Model.CommonModuleP.Base_PublishLablesF import PublishLablesModel;
from app.Service.BusinessP.BaseUtilityF import baseBllManager
from app.Service.RepositoryP.RepositoryF import Repository

# 发布信息标签的 业务逻辑层
class Base_PublishLablesBll(Repository):

    """
        获取所有的publish_lables
        返回格式为(id,name);
    """
    def GetAllLables(self):
        session = baseBllManager.GetConn()();
        result = session.query(PublishLablesModel.id,PublishLablesModel.name).filter().all()

        '''
        提交保存后 可以直接获取ID
        publishLablesModel = PublishLablesModel()
        publishLablesModel.name = "农具"
        session.add(publishLablesModel);
        session.commit();
        print(publishLablesModel.id);
        '''
        session.close();

        result.insert(0,('id', 'name'))
        return result;
