from django.db import models

class prodDatabase(models.Model):
    prodName = models.CharField(max_length=240)
    prodDescription = models.CharField(max_length=1024)
    prodPrice = models.CharField(max_length=20)
    prodBatch = models.CharField(max_length=20)
    expiryDate = models.CharField(max_length=20)
    isAvailable = models.BooleanField(default=True)
    isPrescriptionRequired = models.BooleanField(default=False)

class Transaction(models.Model):
    orderId = models.IntegerField(max_length=10,default=0)
    orderDate = models.CharField(max_length=10,default='')
    deliveryDate = models.CharField(max_length=10,default='')
    orderStatus = models.CharField(max_length=15,default='')
    noOfItems = models.IntegerField(max_length=10,default=0)


    
