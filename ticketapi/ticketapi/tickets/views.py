from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ticketapi.serializers import UserSerializer, TicketSerializer, CategorySerializer

from django.contrib.auth.models import User
from tickets.models import Ticket, Category
