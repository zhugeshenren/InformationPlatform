# 配置路由，先导入包，然后再添加tuple(元组)
import app.UI.Login.urls
import app.UI.Home.urls
import app.UI.Info.urls
import app.UI.Conversation.urls
import app.UI.My.urls
import app.UI.GeneralPage.urls

urlpattern = ();

urlpattern += app.UI.Login.urls.urlpattern;

urlpattern += app.UI.Home.urls.urlpattern;

urlpattern += app.UI.Info.urls.urlpattern;

urlpattern += app.UI.Conversation.urls.urlpattern;

urlpattern += app.UI.My.urls.urlpattern;

urlpattern += app.UI.GeneralPage.urls.urlpattern;