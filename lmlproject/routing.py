# # mysite/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing
import lmlapp.routing
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
                URLRouter(
                    chat.routing.websocket_urlpatterns
                )
        )
    ),
})