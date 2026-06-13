from netbox.api.routers import NetBoxRouter
from . import views


router = NetBoxRouter()
router.APIRootView = views.PhoneBoxPluginRootView

router.register(r'numbers', views.NumberViewSet)
router.register(r'voice-circuits', views.VoiceCircuitsViewSet)

app_name = "phonebox_plugin-api"
urlpatterns = router.urls
