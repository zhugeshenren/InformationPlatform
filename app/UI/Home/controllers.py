from app.Extension.PublicClass import PublicRequestHandler;
from tornado.web import authenticated

class HomeControllers(PublicRequestHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.render('Home/views/Home.html')



class TestListControllers(PublicRequestHandler):
    @authenticated
    def get(self):
        self.render('Home/views/index.html')