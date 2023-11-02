from rest_framework import viewsets
from .models import Car, Dealer
from .serializers import CarSerializer, DealerSerializer

class CarViewSet(viewsets.ModelViewSet):
    ''' Model View set class for performing CRUD operations for Car Model'''
    queryset = Car.objects.all() # retrieving all the data from database using ORM
    serializer_class = CarSerializer
    
class DealerViewSet(viewsets.ModelViewSet):
    ''' Model View set class for performing CRUD operations for Dealer Model'''
    queryset = Dealer.objects.all() # retrieving all the data from database using ORM
    serializer_class = DealerSerializer
