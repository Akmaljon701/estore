from rest_framework import serializers
from sale.models import Category, Product, Cart, Sale


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['products']


class CartGetSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['products']


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['products', 'phone']
