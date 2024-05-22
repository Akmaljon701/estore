from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from sale.models import Category, Product
from sale.serializers import CategorySerializer, ProductSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=200)


@swagger_auto_schema(method='GET', manual_parameters=[
    openapi.Parameter('category', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False),
])
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
def get_products(request):
    category = request.query_params.get('category')

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    # filter_params = {}
    # if name:
    #     filter_params['name'] = name
    # if CPU:
    #     filter_params['CPU'] = CPU
    # if GPU:
    #     filter_params['GPU'] = GPU
    # if RAM:
    #     filter_params['RAM'] = RAM
    #
    # if filter_params:
    #     products = products.filter(**filter_params)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=200)

