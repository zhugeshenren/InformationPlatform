"""
    描述:
        响应一些通用的http请求
"""

from app.Extension.PublicClass import PublicRequestHandler
from app.Extension.Encryption.TeaAlgo import tea

from app.Extension.Encryption.UniqueKeyOper import uniqueKey
import json

'''
    描述: 
        
'''
class GetUniqueKeyControllers(PublicRequestHandler):

    '''
        从服务器上获取一个key，约定这个key的格式如下
        用户编码 : 年-月日-id
        过期时间 : 年-月日-时-分
        中间使用 "|" 进行分割

    '''
    def post(self, *args, **kwargs):
        data = dict();
        ukey = uniqueKey.encode("2018-0302-100000|2018-0305-15-05");
        data["UniqueKey"] = ukey
        self.write(json.dumps(data))
