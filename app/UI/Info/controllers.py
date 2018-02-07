# 控制器
from app.Extension.PublicClass import PublicRequestHandler

class InfoHomeControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Info/views/InfoHome.html',page_title = '信息');

class InfoNewsControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Info/views/InfoNews.html',page_title = '资讯');