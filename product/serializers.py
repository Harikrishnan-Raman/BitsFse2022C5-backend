from rest_framework import serializers
from .models import prodDatabase, Transaction

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = prodDatabase 
        fields = ('pk', 'prodName', 'prodDescription', 'prodPrice', 'prodBatch', 'expiryDate', 'isAvailable', 'isPrescriptionRequired')

        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields =['orderId','orderDate','deliveryDate','orderStatus','noOfItems']
