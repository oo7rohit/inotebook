from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsAuthor


class NoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = NoteSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor,]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer