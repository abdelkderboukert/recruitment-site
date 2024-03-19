from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('create_cv/', views.create_cv, name='create_cv'),
    path('add/<int:jobID>/', views.add, name='add'),
    path('del_user/', views.del_user, name='del_user'),
]