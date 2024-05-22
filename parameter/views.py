from rest_framework.decorators import api_view
from rest_framework.response import Response
from parameter.models import *
from parameter.serializers import *


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
def get_rams(request):
    rams = RAM.objects.all()
    serializer = RAMSerializer(rams, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
def get_cpus(request):
    cpus = CPU.objects.all()
    serializer = CPUSerializer(cpus, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
def get_gpus(request):
    gpus = GPU.objects.all()
    serializer = GPUSerializer(gpus, many=True)
    return Response(serializer.data, status=200)

