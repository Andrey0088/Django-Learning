from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed', views.feed),
    path('publicate', views.publicate)
]
