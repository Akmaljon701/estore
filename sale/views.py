from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from sale.models import Category, Product, Cart
from sale.serializers import CategorySerializer, ProductSerializer, CartSerializer, CartGetSerializer, SaleSerializer
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

    products = Product.objects.filter(count__gte=0).all()

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


@swagger_auto_schema(method='put', request_body=CartSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def user_add_product_to_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found."}, status=404)

    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        products = serializer.validated_data['products']
        for product in products:
            cart.products.add(product)
        cart.save()
        return Response({"detail": "Products added to cart successfully."}, status=200)
    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(method='delete', request_body=CartSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def user_remove_product_from_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found."}, status=404)

    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        products = serializer.validated_data['products']
        for product in products:
            cart.products.remove(product)
        cart.save()
        return Response({"detail": "Products removed from cart successfully."}, status=200)
    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def user_get_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found."}, status=404)

    for product in cart.products.all():
        if product.count <= 0:
            cart.products.remove(product)
    cart.save()

    serializer = CartGetSerializer(cart)
    return Response(serializer.data, status=200)


@swagger_auto_schema(method='post', request_body=SaleSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def user_sale(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found."}, status=404)

    serializer = SaleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        products = serializer.validated_data['products']
        for product in products:
            if product.count <= 0:
                return Response({"detail": "Product count is not sufficient."}, status=400)
            cart.products.remove(product)
        cart.save()
        return Response({"detail": "Sale created and products removed from cart successfully."},
                        status=201)
    else:
        return Response(serializer.errors, status=400)

