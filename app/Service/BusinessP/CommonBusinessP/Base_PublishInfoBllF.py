from app.Model.CommonModuleP.Base_PublishInfoLablesF import PublishInfoLablesModel

from app.Service.BusinessP.BaseUtilityF import baseBllManager
from app.Service.RepositoryP.RepositoryF import Repository
from app.Extension.DecodeData import decodeHtmlBody

class Base_PublishInfoLablesBll(Repository):

    '''
        保存PublishInfo的数据
    '''
    def SavePublishInfo(self,body):

        dictData = decodeHtmlBody.DecodeBody(body);


        return 1;
