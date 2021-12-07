from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing
import stock.routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns + stock.routing.websocket_urlpatterns
        )
    )
})