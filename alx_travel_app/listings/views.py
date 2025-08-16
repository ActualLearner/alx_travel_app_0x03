from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking

# Create your views here.


class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(host=self.request.user)
    
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    