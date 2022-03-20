from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from library.models import HealthStatus, Checkbox

from library.views import (
    UserViewSet, HealthStatusViewSet, CheckboxViewSet
)

router = DefaultRouter()
router.register(
    prefix='health_status', viewset=HealthStatusViewSet, basename='health_status',
)
router.register(
    prefix='checkboxes', viewset=CheckboxViewSet, basename='checkboxes',
)
# router.register(
#     prefix='reviews', viewset=ReviewViewSet, basename='reviews',
# )
# router.register(
#     prefix='saved_books', viewset=SavedBookViewSet, basename='saved_books',
# )
# router.register(
#     prefix='genres', viewset=GenreViewSet, basename='genres',
# )
router.register(
    prefix='users', viewset=UserViewSet, basename='users',
)
urlpatterns = router.urls + [
    path(route='auth/', view=csrf_exempt(ObtainAuthToken.as_view())),
]
