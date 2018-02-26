from sqlalchemy.sql.elements import and_

from app.Model.CommonModuleP.Base_UserF import UserModel
from sqlalchemy.orm import sessionmaker;

from app.Model.CommonModuleP.Base_PublishLablesF import PublishLablesModel;
from app.Service.BusinessP.BaseUtilityF import baseBllManager
from app.Service.RepositoryP.RepositoryF import Repository

# 发布信息标签的 业务逻辑层
class Base_PublishLablesBll(Repository):
    def GetAllLables(self):
        session = baseBllManager.GetConn()();
        result = session.query(PublishLablesModel.id,PublishLablesModel.name).filter().all()
        session.close();
        result.insert(0,('id', 'name'))
        return result;
