from django.db import models
from res_framework import serializers

from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Order
        fields=('user')