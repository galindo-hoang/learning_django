from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WatchListAV, WatchDetailAV, StreamPlatformVS, ReviewDetailAV, ReviewAV, ReviewCreateAV

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename="stream-platform")

urlpatterns = [
    path('movie/', WatchListAV.as_view(), name='listWatchMate'),
    path('movie/<int:pk>', WatchDetailAV.as_view(), name='detailWatchMate'),

    path('', include(router.urls)),

    path('stream/<int:pk>/review', ReviewAV.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create', ReviewCreateAV.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetailAV.as_view(), name='review-list'),
]
