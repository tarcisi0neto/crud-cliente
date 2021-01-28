
from django.contrib import admin
from django.urls import path
from usuarios import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
]
