from channels.routing import ProtocolTypeRouter, URLRouter
import alarm.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        alarm.routing.websocket_urlpatterns
    )
})