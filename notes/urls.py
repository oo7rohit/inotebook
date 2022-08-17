from django.urls import path
from .views import NoteList, NoteDetail, UserDetail, UserList

urlpatterns = [
    path('<int:pk>/', NoteDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('', NoteList.as_view()),
]