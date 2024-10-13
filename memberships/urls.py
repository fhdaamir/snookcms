from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

