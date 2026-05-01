
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import SystemInfo, Schedule
from .serializers import (
    SystemInfoSerializer,
    ScheduleSerializer,
    RegisterSerializer
)


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def system_info_update(request, pk):
    try:
        info = SystemInfo.objects.get(pk=pk)
    except SystemInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SystemInfoSerializer(info, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def system_info_partial_update(request, pk):
    try:
        info = SystemInfo.objects.get(pk=pk)
    except SystemInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SystemInfoSerializer(info, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def system_info_delete(request, pk):
    try:
        info = SystemInfo.objects.get(pk=pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except SystemInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedule_list(request):
    schedules = Schedule.objects.filter(user=request.user)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def schedule_create(request):
    data = request.data.copy()
    data['user'] = request.user.id

    serializer = ScheduleSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({
            "message": "User registered successfully",
            "token": token.key,
            "username": user.username
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key,
            "username": user.username
        }, status=status.HTTP_200_OK)

    return Response(
        {"error": "Invalid username or password"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "message": "Authorized access",
        "user": request.user.username
    })



      
    

    