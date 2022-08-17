from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Note


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']