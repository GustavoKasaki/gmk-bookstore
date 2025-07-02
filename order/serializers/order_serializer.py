from rest_framework import serializers

from product.serializers.product_serializer import ProductSerializer
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        total = sum([product.price for product in obj.product.all()])
        return total

    class Meta:
        model = Order
        fields = ['product', 'total']