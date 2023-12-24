
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    #ModelOBj ==> Python Native
    #Python Native ==> ModelObj
    class Meta:
        model = Customer
        fields = "__all__"

