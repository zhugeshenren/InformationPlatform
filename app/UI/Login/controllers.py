from app.Extension.PublicClass import PublicRequestHandler;

from concurrent.futures import ThreadPoolExecutor

import tornado.gen
import tornado.web
import tornado.concurrent

from app.Service.BusinessP.CommonBusinessP.Base_UsersBllF import Base_UserBll

import time

# 创建一个业务处理对象
base_userbll = Base_UserBll();



class LoginControllers(PublicRequestHandler):


    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield self.render_page()

    # 异步返回页面，这个就不使用线程池了
    @tornado.gen.coroutine
    def render_page(self):
        self.render('Login/views/Login.html', page_title="登录");


class LoginProofControllers(PublicRequestHandler):

    # 在这定义一个线程池的原因在于，在 装饰器 @tornado.concurrent.run_on_executor 中 要使用 getattr() 方法调用 线程池 executor

    executor = ThreadPoolExecutor(15)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):

        password = self.get_argument('password');
        username = self.get_argument('username');

        print(password + username)
        result = yield self.check_user(username,password);

        # cookie 名称，内容，退出过期，保持时间
        if result:
            self.set_secure_cookie("user", username,expires_days=None);

        # 渲染文件并且返回给
        #self.render("Home\\views\\Home.html",t1 = "11",t2 = "222")
        # 重定向, URL的设置也是十分有讲究的 \n //
        self.redirect("/Home")

    # 将所有的耗时方法放入 异步线程池中
    @tornado.concurrent.run_on_executor()
    def check_user(self,password,username):
        return base_userbll.CheckUser(password,username);


class RegisterControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Login/views/Register.html',page_title = '注册');



class RetrievePasswordControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Login/views/RetrievePassword.html', page_title='找回密码');

