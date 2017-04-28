from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from git.views import UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, base_name='user')

urlpatterns = [
    url('', include(router.urls))
]