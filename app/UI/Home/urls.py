from app.UI.Home.controllers import (
    HomeControllers,
    TestListControllers,
)

urlpattern = (
    (r'/Home/?',HomeControllers),
    (r'/Home/index',TestListControllers),
);
