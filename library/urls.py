from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from library.models import HealthStatus, Checkbox

from library.views import (
    UserViewSet, HealthStatusViewSet, CheckboxViewSet, PostViewSet, CommentViewSet,
    CustomAuthToken, UserBadgeViews, TestViewSet
)

router = DefaultRouter()
router.register(
    prefix='health_status', viewset=HealthStatusViewSet, basename='health_status',
)
router.register(
    prefix='checkboxes', viewset=CheckboxViewSet, basename='checkboxes',
)
router.register(
    prefix='posts', viewset=PostViewSet, basename='post',
)
router.register(
    prefix='comments', viewset=CommentViewSet, basename='comments',
)
router.register(
    prefix='user_badges', viewset=UserBadgeViews, basename='user_badges',
)
router.register(
    prefix='test', viewset=TestViewSet, basename='test',
)
router.register(
    prefix='users', viewset=UserViewSet, basename='users',
)
urlpatterns = router.urls + [
    path(route='auth/', view=csrf_exempt(CustomAuthToken.as_view())),
]
