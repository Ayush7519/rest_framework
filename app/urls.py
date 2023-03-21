from django.urls import path,include
from . import views
# urlpatterns = [
#     path('api/create/',views.hostcreateapiview.as_view())
# ]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api',views.hostcreateapiview)

urlpatterns = [
    path('', include(router.urls))
]