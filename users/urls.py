from django.urls import path
from .views import UserListView
from .views import CurrentUserView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
]
