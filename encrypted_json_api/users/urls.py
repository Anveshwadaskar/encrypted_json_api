# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('list/', views.UserListView.as_view(), name='user-list'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'),
]
