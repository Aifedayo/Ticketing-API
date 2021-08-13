from rest_framework import serializers

from django.contrib.auth.models import User
from tickets.models import Ticket, Category

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
'''
# Rewriting our UserSerializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = (
                    'id', 'title', 'ticket_id', 
                    'user', 'content', 'category', 'created', 'modified'
                )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
