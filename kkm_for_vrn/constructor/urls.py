from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views.cb_views import TicketViewSet

router = DefaultRouter()
router.register('ticket', TicketViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]