from app.UI.Info.controllers import (
    InfoHomeControllers,
    InfoNewsControllers
)

urlpattern = (
    (r'/InfoHome/?',InfoHomeControllers),
    (r'/Info/InfoNews/?',InfoNewsControllers),
)