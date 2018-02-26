from app.Extension.PublicClass import PublicRequestHandler
import json
from urllib.parse import unquote
import os
from tornado.escape import json_decode
import re
from app.Extension.DecodeData import decodeHtmlBody
from tornado.web import authenticated

from app.Service.BusinessP.CommonBusinessP.Base_PublishLablesBllF import Base_PublishLablesBll

base_PublishLablesBll = Base_PublishLablesBll();

class MyPublishControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/MyPublish.html',page_title = '我的发布');


# 添加Html给 '我的发布'
class AddMyPublishHtmlControllers(PublicRequestHandler):

    # 响应ajax请求
    def post(self, *args, **kwargs):
        pass

    # 允许跨域请求
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()


class AddMyPublishControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        '''
        if not globalDict.Find(self.current_user) is None:
            self.render('My/views/AddMyPublish.html');
        '''
        self.render('My/views/AddMyPublish.html',page_title = '编辑');


# 添加发布标题信息
class AddMyPublishTitleInfoControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/AddMyPublishTitleInfo.html',page_title = '发布标题')

    # 响应Add添加
    def post(self, *args, **kwargs):

        # 解析json TMD解析类竟然需要我自己写

        print(self.request.body)
        dictdata = decodeHtmlBody.DecodeBody(self.request.body)

        print(dictdata)
        # 进行URL解码
        # 返回一个json
        resvalue = {'nextUrl': '/My/MyPublish/AddMyPublish'};
        self.write(json.dumps(resvalue))
        #globalDict.Insert(self.current_user,'True');
        #print(globalDict.Find(self.current_user))
        self.finish();


# 获取publis_lables标签的所有数据
class GetPublishLablesControllers(PublicRequestHandler):
    def post(self, *args, **kwargs):

        # 耗时的IO操作
        result = base_PublishLablesBll.GetAllLables()

        # 将python对象转化为json格式
        self.write(json.dumps(result,ensure_ascii=False))

        print(result);




