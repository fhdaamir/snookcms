from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Member, Booking
from .serializers import MemberSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
