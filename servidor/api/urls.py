from django.urls import path, include
from .views import (
    ProductoListApiView,
)

urlpatterns = [
    path('producto', ProductoListApiView.as_view()),
]