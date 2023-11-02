from django.db import models

class Dealer(models.Model):
    '''Model class for Dealer details'''
    dealer_name = models.CharField(max_length=100)
    
class Car(models.Model):
    '''Model class for Car details'''
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='cars')
