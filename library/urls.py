from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

from library.views import (
    BookViewSet, RentedBookViewSet, ReviewViewSet, SavedBookViewSet,
    UserViewSet, GenreViewSet,
)

router = DefaultRouter()
router.register(
    prefix='books', viewset=BookViewSet, basename='books',
)
router.register(
    prefix='rented_books', viewset=RentedBookViewSet, basename='rented_books',
)
router.register(
    prefix='reviews', viewset=ReviewViewSet, basename='reviews',
)
router.register(
    prefix='saved_books', viewset=SavedBookViewSet, basename='saved_books',
)
router.register(
    prefix='genres', viewset=GenreViewSet, basename='genres',
)
router.register(
    prefix='users', viewset=UserViewSet, basename='users',
)
urlpatterns = router.urls + [
    path(route='auth/', view=csrf_exempt(ObtainAuthToken.as_view())),
]
