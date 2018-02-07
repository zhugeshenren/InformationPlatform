from app.UI.Login.controllers import (
    LoginControllers,
    LoginProofControllers,
    RegisterControllers,
    RetrievePasswordControllers
)

urlpattern = ((r'/Login/?', LoginControllers),
              (r'/Login/Proof',LoginProofControllers),
              (r'/Register',RegisterControllers),
              (r'/RetrievePassword',RetrievePasswordControllers)
              );
