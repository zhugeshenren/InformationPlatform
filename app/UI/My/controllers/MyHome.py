from app.Extension.PublicClass import PublicRequestHandler

class MyHomeControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('My/views/MyHome.html',page_title = '我的');