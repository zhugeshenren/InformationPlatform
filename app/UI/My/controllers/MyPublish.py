from app.Extension.PublicClass import PublicRequestHandler
import json
from urllib.parse import unquote
from app.Extension.GlobalVar import (
    globalDict
)


class MyPublishControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/MyPublish.html',page_title = '我的发布');

class AddMyPublishControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        '''
        if not globalDict.Find(self.current_user) is None:
            self.render('My/views/AddMyPublish.html');
        '''
        self.render('My/views/AddMyPublish.html');


class AddMyPublishTitleInfoControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/AddMyPublishTitleInfo.html',page_title = '发布标题')

    # 响应Add添加
    def post(self, *args, **kwargs):
        data = self.request.body;
        print(data)

        # 进行URL解码
        unquote('xml=%E6%9F%B1%E5%93%A5&dr=ak');

        # 返回一个json
        resvalue = {'nextUrl': '/My/MyPublish/AddMyPublish'};

        self.write(json.dumps(resvalue))
        globalDict.Insert(self.current_user,'True');
        print(globalDict.Find(self.current_user))
        self.finish();