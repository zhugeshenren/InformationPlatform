from app.Extension.PublicClass import PublicRequestHandler
import json
from urllib.parse import unquote
import os
from tornado.escape import json_decode
import re
from app.Extension.DecodeData import decodeHtmlBody
from tornado.web import authenticated

class MyPublishControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/MyPublish.html',page_title = '我的发布');

# 响应添加图片请求 通过设置headers让其支持跨域, 实际应用中这一部分功能是要搬到其他服务器上的
# #必须优化
class AddMyPublishImgControllers(PublicRequestHandler):
    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

    # 允许http 跨域
    def set_default_headers(self):
        print("setting headers")
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名，进行限制
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # 返回json 用于回显
    def post(self, *args, **kwargs):
        upload_path = 'C:/Users/Administrator/Desktop/农/Code/InformationPlatform/static/files'  # 文件的暂存路径
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        print(upload_path)
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])

        tmp = {"status": 1,"url": ""};
        # 返回地址
        tmp['url'] = 'http://47.94.128.163:8000/static/files/'+filename;
        self.write(json.dumps(tmp));

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
    @authenticated
    def post(self, *args, **kwargs):

        # 解析json TMD解析类竟然需要我自己写
        dictdata = decodeHtmlBody.DecodeBody(self.request.body)
        print(dictdata)

        # 进行URL解码
        # 返回一个json
        resvalue = {'nextUrl': '/My/MyPublish/AddMyPublish'};
        self.write(json.dumps(resvalue))
        #globalDict.Insert(self.current_user,'True');
        #print(globalDict.Find(self.current_user))
        self.finish();


