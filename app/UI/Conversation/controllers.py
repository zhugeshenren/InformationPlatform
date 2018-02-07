from app.Extension.PublicClass import PublicRequestHandler

class ConversationHomeControllers(PublicRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Conversation/views/ConversationHome.html',page_title = '会话');