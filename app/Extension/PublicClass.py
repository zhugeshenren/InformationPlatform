import tornado.web

# 重点 : 类名不要与文件名重复

# 事实上这是一个拦截器的实现，我们通过继承 tornado.web.RequestHandler 方法实现了 initialize，这将会在每一次响应http请求之前被调用

class PublicRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        print("触发了了拦截器")

    # 判断cookies
    def get_current_user(self):
        return self.get_secure_cookie("user");
