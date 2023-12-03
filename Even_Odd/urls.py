from django.contrib import admin
from django.urls import path
from Even_Odd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
