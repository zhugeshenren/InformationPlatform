import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from  Project.urls import urlpattern;
import os.path;

from tornado.options import define, options
from app.Model.CommonModuleP.Base_UserF import UserModel
from app.Service.BusinessP.BaseUtilityF import BaseBllManager;

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine

from app.Extension.GlobalVar import (
    GlobalDict
)


define("port", default=8000, help="run on the given port", type=int)


# 先写框架，再优化

if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = tornado.web.Application(  handlers=urlpattern,
                                    static_path=os.path.join(os.path.dirname(__file__), "static"),  # 这里增加设置了静态路径
                                    template_path = os.path.join(os.path.dirname(__file__), "app/UI"),
                                    debug=True,

                                    # 控制登录拦截
                                    cookie_secret="xuexuebaixuexuebai",
                                    login_url = '/Login'
                                  )


    # 创建一个数据库连接池，作为一个全局变量
    ConnStr = 'mysql+pymysql://root:123456@localhost:3306/infoplatformdb';
    BaseBllManager().SetConn(ConnStr);

    # 巧妙地通过 Configurable的 __new__方法构造了对象
    http_server = tornado.httpserver.HTTPServer(app);

    # 开始监听
    http_server.listen(options.port)

    # 开始循环
    tornado.ioloop.IOLoop.instance().start()