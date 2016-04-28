from django.conf.urls import url, include
from sisbazar.views.PersonaView import PersonaViewSet
from rest_framework import routers

#Create a router and register our viewsets with it.
router = routers.DefaultRouter()
#router.register(r'snippets', SnippetViewSet)
router.register(r'personas', PersonaViewSet)
#router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
