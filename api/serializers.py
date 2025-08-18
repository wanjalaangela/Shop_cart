# Code to create a serializer for the product
from rest_framework import serializers
from catalogue.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
