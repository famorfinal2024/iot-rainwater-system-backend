# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SystemInfo, Schedule
from .serializers import SystemInfoSerializer, ScheduleSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SystemInfo, Schedule
from .serializers import SystemInfoSerializer, ScheduleSerializer

# System Info Endpoints
@api_view(['GET'])
def system_info_list(request):
    infos = SystemInfo.objects.all()
    serializer = SystemInfoSerializer(infos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def system_info_create(request):
    serializer = SystemInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# Schedule Endpoints
@api_view(['GET'])
def schedule_list(request):
    schedules = Schedule.objects.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def schedule_create(request):
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# Protected Example (authentication required)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "Authorized"})