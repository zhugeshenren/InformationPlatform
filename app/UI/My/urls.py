from app.UI.My.controllers.MyHome import (
    MyHomeControllers,
)

from app.UI.My.controllers.MyPublish import (
    MyPublishControllers,
    AddMyPublishControllers,
    AddMyPublishTitleInfoControllers,
    AddMyPublishHtmlControllers,
    GetPublishLablesControllers,
)

urlpattern = (
    (r'/MyHome/?',MyHomeControllers),
    (r'/My/MyPublish/?',MyPublishControllers),
    (r'/My/MyPublish/AddMyPublish/?',AddMyPublishControllers),
    (r'/My/MyPublish/AddMyPublishTitleInfo/?',AddMyPublishTitleInfoControllers),
    (r'/My/MyPublish/AddMyPublish/AddHtml/?',AddMyPublishHtmlControllers),
    (r'/My/MyPublish/GetPublishLables/?',GetPublishLablesControllers),
)