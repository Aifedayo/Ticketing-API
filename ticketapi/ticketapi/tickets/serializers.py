from rest_framework import serializers

from django.contrib.auth.models import User
from tickets.models import Ticket, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')