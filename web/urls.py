from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name= 'logout'),
    path('register/', views.register_user, name= 'register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('add/', views.add_record, name='add'),
    path('update/<int:pk>', views.update, name='update'),
]