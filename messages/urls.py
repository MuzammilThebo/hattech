from django.contrib import admin
from django.urls import path
from whatsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message', views.message),    # ← new item
]