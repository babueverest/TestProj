from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'owner', api.OwnerViewSet)
router.register(r'pet', api.PetViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)
