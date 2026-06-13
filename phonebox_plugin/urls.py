from django.urls import include, path
from utilities.urls import get_model_urls

# Importing views registers their @register_model_view URL paths.
from . import views  # noqa: F401

urlpatterns = [
    # Numbers
    path('numbers/', include(get_model_urls('phonebox_plugin', 'number', detail=False))),
    path('numbers/<int:pk>/', include(get_model_urls('phonebox_plugin', 'number'))),

    # Voice circuits
    path('voice-circuits/', include(get_model_urls('phonebox_plugin', 'voicecircuit', detail=False))),
    path('voice-circuits/<int:pk>/', include(get_model_urls('phonebox_plugin', 'voicecircuit'))),
]
