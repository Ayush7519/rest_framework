from django.urls import path
from . import views
urlpatterns = [
    path('api/create/',views.hostcreateapiview.as_view())
]